
from django.shortcuts import render
from django.http import HttpResponse
from _datetime import datetime



import booking.models as model
import random


def homepage(request):
    return render(request, 'homepage.html', {})


def search(request):

    if request.method == 'GET':
        if not request.GET:
            return render(request, 'search.html', {})
        else:
            response = request.GET

            # Convert input strings to date objects for filtering
            from_date = convert_to_date(response.get('from_date'))
            to_date = convert_to_date(response.get('to_date'))


            # filter all the schedule in the date range
            schedules = model.Schedule.objects.filter(
                depDate__date__range=(from_date, to_date),
                origin=response.get('origin'),
                dest=response.get('destination')
            ).values('schedId', 'flightNo', 'depDate', 'arrDate','seats', 'price')

            # Retrieve customer data that will be passed with the search result
            customers = model.Customer.objects.all()

            #create additional contexts to be rendered on the browser
            context = {
                'schedules': schedules,
                'customers': customers,
                'origin': model.Airport.objects.get(code=response.get('origin')).name,
                'dest': model.Airport.objects.get(code=response.get('destination')).name,
                'from_date': from_date,
                'to_date': to_date
            }

            # checks if there are flight schedules for the date range provided
            if schedules:
                return render(request, 'search.html', context)
            else:
                error = {'Message': 'No flight schedules found for the date range provided. Please check other dates! '}
                return render(request, 'search.html', {'message': error})

    elif request.method == 'POST':

        # Get submitted date from the browser
        schedule_id = request.POST.get('scheid')
        customer_id = request.POST.get('customers')

        # Generate a random three-digit number, for booking reference
        n = random.randint(100, 999)

        #Generate a unique booking reference
        booking_ref = 'BK-CUS' + str(customer_id) + '-SCH' + str(schedule_id) + "-" + str(n)

        while model.Booking.objects.filter(booking_ref= booking_ref).exists():
            n = random.randint(100, 999)
            booking_ref = 'BK-CUS' + str(customer_id) + '-SCH' + str(schedule_id) + "-" + str(n)

        schedule = model.Schedule.objects.get(schedId=schedule_id)


        #Check if the seat count is greater than 1
        if schedule.seats > 0:
            try:
                booking = model.Booking(customer_id, schedule_id, booking_ref)
                booking.save()
                customer = model.Customer.objects.get(id = customer_id)

                invoice_data = generate_booking_summary(customer,schedule,booking)

                # Every time booking is made, subtract the seat by 1!
                schedule.seats -= 1
                schedule.save()
                return render(request, 'invoice.html', {'invoice': invoice_data})

            except Exception as e:
                error = {'Message': f'Booking failed: {str(e)}'}
                return render(request, 'search.html', {'message':error})

        else:
            error = {'Message': 'No Seats available in this flight, please try a different one'}
            return render(request, 'search.html', {'message': error})

    else:
        return HttpResponse("Method not allowed", status=405)


def managebooking(request):
    if request.method == 'GET':

        return render(request, 'manage.html', {})

    elif request.method == 'POST':
        booking_id = request.POST.get('booking_ref')

        try:
            booking_reference = model.Booking.objects.get(booking_ref=booking_id)
        except model.Booking.DoesNotExist :
            bookings = model.Booking.objects.all()
            error = {'message': 'Booking reference not found. Please try again!'}
            return render(request, 'manage.html', {'message': error})

        schedule = booking_reference.schedule
        customer = booking_reference.customer

        try:

            # Collect booking info BEFORE deletion
            booking_deletion_response = generate_booking_summary(customer, schedule, booking_reference)
            booking_reference.delete()
            schedule.seats += 1
            schedule.save()


            bookings = model.Booking.objects.all()
            return render(request, 'manage.html', {
                'booking_deletion_response': booking_deletion_response
            })

        except Exception as e:
            print("Error:", e)
            bookings = model.Booking.objects.all()
            error = {'Message': 'An unexpected error occurred.'}
            return render(request, 'manage.html', {'message': error})


def invoice(request):
    if not request.GET:
        return render(request, 'invoice.html', {})

    data= request.GET.get('booking_ref')

    #Convert received booking reference to uppercase
    booking_ref =data.upper()

    try:
        booking = model.Booking.objects.get(booking_ref=booking_ref)
    except model.Booking.DoesNotExist:
        error = {'Message': 'Booking reference not found. Please try again!'}
        return render(request, 'invoice.html',{'message': error})

    customer= booking.customer
    schedule = booking.schedule


    invoice_data = generate_booking_summary(customer,schedule,booking)

    return render(request, 'invoice.html', {'invoice': invoice_data})

def contactus(request):
    return render(request, 'contactus.html', {})





# convert date string to date
def convert_to_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.date()
    except (TypeError, ValueError):
        return  None

#Function to create an appropriate data list for invoice, booking cancellation data creation
def generate_booking_summary(customer, schedule, booking):
    booking_data_context = {
        'Booking Reference': booking.booking_ref,
        'Name': f"{customer.salutation} {customer.firstname} {customer.lastname}",
        'Schedule ID': schedule.schedId,
        'Flight Number': schedule.flightNo,
        'Origin': model.Airport.objects.get(code= schedule.origin.code).name,
        'Destination': model.Airport.objects.get(code=schedule.dest.code).name,
        'Departure': schedule.depDate,
        'Arrival': schedule.arrDate,
        'Price': schedule.price
    }

    return booking_data_context