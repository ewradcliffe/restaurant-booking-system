from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('reservation_name', 'reservation_date', 'reservation_time', 'number_of_guests',)
