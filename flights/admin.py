from django.contrib import admin

from .models import *
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_ = ("flights", )

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)