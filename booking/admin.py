from booking.models import Table, Reservation
from django.contrib import admin


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'seats_amount', 'is_reserved',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'date', 'time', 'client')
