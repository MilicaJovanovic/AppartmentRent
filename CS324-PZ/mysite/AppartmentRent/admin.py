from django.contrib import admin

from .models import Appartment, Reservation, Location, Contact

class ReservationAdmin(admin.ModelAdmin):
    list_filter = ['start_date']

admin.site.register(Location)
admin.site.register(Appartment)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Contact)