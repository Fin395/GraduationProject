from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from booking.mixins import StyleFormMixin
from booking.models import Reservation


class ReservationForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'client', 'date', 'time']
        widgets = {
            'date': forms.SelectDateWidget(),  # Используем виджет выбора даты
        }

    def clean_date(self):
        data = self.cleaned_data['date']

        if data < date.today():
            raise ValidationError('Вы не можете выбрать прошедшую дату для бронирования.')

        return data