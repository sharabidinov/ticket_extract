from django.contrib import admin
from .models import Flight, Ticket


# Register your models here.


class FlightInline(admin.StackedInline):
    model = Flight
    extra = 0


class FlightAdmin(admin.ModelAdmin):
    inlines = [FlightInline]
    list_display = ['pnr_number', 'first_name', 'last_name']


admin.site.register(Ticket, FlightAdmin)
