from celery import shared_task
from django.utils import timezone

from booking.models import Reservation


@shared_task
def change_reservation_status():
    today = timezone.now().date()
    reservations = Reservation.objects.filter(status="Открыта", date=today)
    reservations.update(status="Закрыта")
