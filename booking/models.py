from django.db import models

from users.models import User


class Table(models.Model):
    seats_amount = models.PositiveSmallIntegerField(verbose_name='Количество мест')
    is_reserved = models.BooleanField(verbose_name='Резерв', default=False)

    def __str__(self):
        return f'Столик № {self.pk}'

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'


class Reservation(models.Model):
    TIME_CHOICES = [
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
        ('22:00', '22:00'),
        ('23:00', '23:00'),
    ]

    time = models.CharField(max_length=5, choices=TIME_CHOICES, default='10:00', verbose_name='Время')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='tables', verbose_name='Столик')
    date = models.DateField(verbose_name='Дата')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', verbose_name='Клиент', blank=True, null=True)

    def __str__(self):
        return f'Бронь на {self.date} в {self.time}'

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

