from booking.models import Table
from django.contrib import admin



@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'seats_amount', 'is_reserved',)
