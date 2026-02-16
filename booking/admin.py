from django.contrib import admin

from booking.models import Reservation, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "seats_amount",
    )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "table", "date", "time", "owner", "status")
