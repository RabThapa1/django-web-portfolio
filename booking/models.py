from django.db import models
from django.db.models import CASCADE


# Create your tests here.

class Airport(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=55)
    region = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Airport'

class Schedule(models.Model):
    schedId    = models.IntegerField(primary_key=True)
    flightNo   = models.CharField(max_length= 5)
    origin     = models.ForeignKey(Airport,
                                 related_name= 'origin',
                                on_delete= CASCADE)
    dest       = models.ForeignKey(Airport,
                                   related_name= 'dest',
                                   on_delete=CASCADE)
    depDate    = models.DateTimeField()
    arrDate    = models.DateTimeField()
    flightTime = models.TimeField()
    seats      = models.IntegerField(default=0)
    price      = models.DecimalField(max_digits=6,null=True, decimal_places=2)

    def __str__(self):
        return self.flightNo

    class Meta:
        db_table = 'Schedule'



class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    salutation = models.CharField(max_length=3)
    firstname  = models.CharField(max_length= 10)
    lastname   = models.CharField(max_length=10)
    gender     = models.CharField(max_length=1)
    email      = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        db_table = 'Customer'


class Booking(models.Model):
    customer = models.ForeignKey(Customer,
                                   related_name='customer_bookings',
                                   on_delete=CASCADE)
    schedule = models.ForeignKey(Schedule,
                                   related_name='schedule_bookings',
                                   on_delete=CASCADE)

    booking_ref = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return f"Booking for {self.customer} on {self.schedule}"

    class Meta:
        db_table = 'Booking'

