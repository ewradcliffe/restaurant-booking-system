from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):

    def test_form_is_valid(self):
        reservation_form = ReservationForm({'reservation_name': 'Joe Bloggs', 
                                            'reservation_date': '2024-09-30', 
                                            'reservation_time': '13:00', 
                                            'number_of_guests': '2'})
        self.assertTrue(reservation_form.is_valid())