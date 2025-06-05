from django.contrib import admin

# Register your models here.
from booking.models import Airport, Schedule, Customer, Booking

admin.site.register(Airport)
admin.site.register(Schedule)
admin.site.register(Customer)
admin.site.register(Booking)