from django.db import models


class Table(models.Model):
    seats_amount = models.PositiveSmallIntegerField(verbose_name='Количество мест')
    is_reserved = models.BooleanField(verbose_name='Резерв', default=False)

    def __str__(self):
        return f'Столик № {self.pk}'

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'
