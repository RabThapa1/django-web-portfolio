import os
import csv
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airline_booking.settings")
import django
django.setup()

import booking.models as models


def set_airport():
    airports = [
        ('NZNE', 'North Shore Dairy Flat Airport', 'Auckland North Shore'),
        ('NZRO', 'Rotorua Airport', 'Rotorua / Bay of Plenty'),
        ('NZCI', 'Tuuta Airport', 'Chatham Islands'),
        ('NZGB', 'Claris Airport', 'Great Barrier Island'),
        ('NZTL', 'Lake Tekapo Airport', 'Mackenzie Airport'),
        ('YMML', 'Melbourne Airport', 'Victoria Australia')
    ]

    for info in airports:
        print(info)
        a = models.Airport(*info)
        a.save()

def set_schedule():


    date = datetime(2025, 5, 5)

    schedule = [
   # Ensures the same flight number isn't scheduled multiple times for the same departure date and time
   #Flightno, origin, destination, dept time, arrival time, flight duration ,pricing and operating days


    ('SJ102', 'NZNE', 'YMML', '10:00:00', '14:00:00','04:00:00' ,300, 6, [4]),
    ('SJ201', 'YMML', 'NZNE', '14:00:00', '20:00:00','04:00:00',300, 6, [6]),
    ('CJ102', 'NZNE', 'NZRO', '08:00:00', '08:45:00','00:45:00', 120, 4, [0, 1, 2, 3, 4]),
    ('CJ201', 'NZRO', 'NZNE', '11:00:00', '11:45:00','00:45:00', 120, 4, [0, 1, 2, 3, 4]),
    ('CJ301', 'NZNE', 'NZRO', '16:00:00', '16:45:00','00:45:00', 120, 4, [0, 1, 2, 3, 4]),
    ('CJ402', 'NZRO', 'NZNE', '18:00:00', '18:45:00','00:45:00', 120, 4, [0, 1, 2, 3, 4]),
    ('CJ502', 'NZNE', 'NZGB', '09:00:00', '09:30:00','00:30:00', 145, 4, [0, 2, 4]),
    ('CJ604', 'NZGB', 'NZNE', '10:00:00', '10:30:00','00:30:00',145, 4, [1, 3, 5]),
    ('HJ409', 'NZNE', 'NZCI', '12:00:00', '14:45:00','02:00:00',200, 5, [1, 4]),
    ('HJ510', 'NZCI', 'NZNE', '14:00:00', '15:15:00','02:00:00',200, 5, [2, 5]),
    ('HJ810', 'NZNE', 'NZTL', '11:00:00', '12:25:00','01:25:00',160,5, [0]),
    ('HJ910', 'NZTL', 'NZNE', '13:00:00', '14:25:00','01:25:00', 160,5, [1])

    ]

    end_date = date + timedelta(110)
    schedule_id = 10

    while date < end_date:
        weekday = date.weekday()


        for flightNo, origin, destination, dep_time, arr_time,flight_duration_str, price, seats, operating_days in schedule:

            #Fetch Airport objects
            try:
                origin_airport = models.Airport.objects.get(code=origin)
                destination_airport = models.Airport.objects.get(code=destination)
            except Exception as e:
                print('Error:',e)

            # Convert departure and arrival times
            depDate = datetime.combine(date, datetime.strptime(dep_time, "%H:%M:%S").time())
            arrDate = datetime.combine(date, datetime.strptime(arr_time, "%H:%M:%S").time())

            # Convert flight duration string to timedelta
            flight_duration = datetime.strptime(str(flight_duration_str), '%H:%M:%S').time()


            if weekday in operating_days:
               try:
                   s = models.Schedule(
                    schedId = schedule_id,
                    flightNo = flightNo,
                    origin=origin_airport,
                    dest= destination_airport,
                    depDate=depDate,
                    arrDate = arrDate,
                    flightTime = flight_duration,
                    seats=seats,
                    price = price
                   )
                   s.save()
                   print(schedule)
                   schedule_id += 1

               except Exception as e:
                   print("Error:" ,e)



        date = date + timedelta(days=1)

def set_customer():
    try:
        with open('randomnames.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
               customer = models.Customer(
                    id=row[0],
                    salutation=row[1],
                    firstname=row[2],
                    lastname=row[3],
                    gender = row[4],
                    email=row[5]
                )
               customer.save()
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    print("Populate Database")
    set_airport()
    set_schedule()
    set_customer()