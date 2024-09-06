from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):
    """
    Tests are derived from The code institute
    'I think therefore I blog' module.
    https://learn.codeinstitute.net/
    """

    def test_form_is_valid(self):
        """
        Tests form is valid.
        """
        reservation_form = ReservationForm({'reservation_name': 'Joe Bloggs',
                                            'reservation_date': '2024-09-30',
                                            'reservation_time': '13:00',
                                            'number_of_guests': '2'})
        self.assertTrue(reservation_form.is_valid())

    def test__name_is_required(self):
        """
        Tests name field.
        """
        reservation_form = ReservationForm({'reservation_name': '',
                                            'reservation_date': '2024-09-30',
                                            'reservation_time': '13:00',
                                            'number_of_guests': '2'})
        self.assertFalse(reservation_form.is_valid(),
                         msg="reservation_name field left blank")

    def test__date_is_required(self):
        """
        Tests date field.
        """
        reservation_form = ReservationForm({'reservation_name': 'Joe Bloggs',
                                            'reservation_date': '',
                                            'reservation_time': '13:00',
                                            'number_of_guests': '2'})
        self.assertFalse(reservation_form.is_valid(),
                         msg="reservation_date field left blank")

    def test__time_is_required(self):
        """
        Tests time field.
        """
        reservation_form = ReservationForm({'reservation_name': 'Joe Bloggs',
                                            'reservation_date': '2024-09-30',
                                            'reservation_time': '',
                                            'number_of_guests': '2'})
        self.assertFalse(reservation_form.is_valid(),
                         msg="reservation_time field left blank")

    def test__number_of_guests_is_required(self):
        """
        Tests number of guests field.
        """
        reservation_form = ReservationForm({'reservation_name': 'Joe Bloggs',
                                            'reservation_date': '2024-09-30',
                                            'reservation_time': '13:00',
                                            'number_of_guests': ''})
        self.assertFalse(reservation_form.is_valid(),
                         msg="number_of_guests field left blank")
