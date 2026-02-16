from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from booking.mixins import StyleFormMixin
from booking.models import Reservation


class ReservationForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "table",
            "date",
            "time",
            "client_name",
            "client_phone_number",
            "client_willing",
        ]
        widgets = {
            "date": forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get("date")
        reservation_time = cleaned_data.get("time")
        reserved_table = cleaned_data.get("table")

        if reservation_date < date.today():
            raise ValidationError(
                "Вы не можете выбрать прошедшую дату для бронирования."
            )

        filtered_reservations = Reservation.objects.filter(
            table=reserved_table,
            date=reservation_date,
            time=reservation_time,
            status="Открыта",
        )
        if filtered_reservations.exists():
            for reservation in filtered_reservations:
                if reservation.owner != self.user:
                    raise ValidationError(
                        "Этот столик уже забронирован в указанные дату и время. "
                        "Пожалуйста, выберите другой столик или время."
                    )

        return cleaned_data
