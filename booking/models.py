from django.db import models

from users.models import User


class Table(models.Model):
    seats_amount = models.PositiveSmallIntegerField(verbose_name="Количество мест")

    def __str__(self):
        return f"Столик № {self.pk}"

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"


class Reservation(models.Model):
    TIME_CHOICES = [
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("19:00", "19:00"),
        ("20:00", "20:00"),
        ("21:00", "21:00"),
        ("22:00", "22:00"),
        ("23:00", "23:00"),
    ]

    ACTUAL = "Открыта"
    CLOSED = "Закрыта"
    CANCELLED = "Отменена"

    RESERVATION_STATUS_CHOICES = [
        (ACTUAL, "Открыта"),
        (CLOSED, "Закрыта"),
        (CANCELLED, "Отменена"),
    ]
    time = models.CharField(
        max_length=5, choices=TIME_CHOICES, default="10:00", verbose_name="Время"
    )
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="tables", verbose_name="Столик"
    )
    date = models.DateField(verbose_name="Дата")
    client_name = models.CharField(
        max_length=35, verbose_name="На чье имя бронь", default="Имя гостя"
    )
    client_phone_number = models.CharField(
        max_length=25,
        verbose_name="Телефон",
        default="Телефон для связи",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="owner_reservations",
    )
    client_willing = models.TextField(
        verbose_name="Пожелания",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=20,
        choices=RESERVATION_STATUS_CHOICES,
        verbose_name="Статус",
        default="Открыта",
    )

    def __str__(self):
        return f"Бронь на {self.date} в {self.time}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
