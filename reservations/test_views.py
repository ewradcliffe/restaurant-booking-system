from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReservationForm
from .models import Reservation



class TestReservationViews(TestCase):
    """
    Tests views for the Reservations app.
    """
    def setUp(self):

        """Sets up an instance of a user"""

        self.user = User.objects.create_user(
            username="username",
            password="password123!",
            email="test@test.com"
        )
        self.user.save()

        """Sets up an instance of a reservation"""
        self.reservation = Reservation(reservation_name='Usertest', reservation_date='2024-12-31' , 
                                        reservation_time = '12:00', number_of_guests='4',  
                                        reservation_booked_by=self.user)          
        self.reservation.save()


    def test_render_index_page(self):
        """
        Tests to see if the index page renders.
        """
        response = self.client.get(reverse('index-urls'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to The Blue Boar Inn.", response.content)


    def test_render_reservation_page(self):
        """
        Tests to see if the reservation page renders.
        """
        self.client.login(username='username', password='password123!')
        response = self.client.get(reverse('reservations-urls'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"You are not logged in", response.content)
        self.assertIn(b"Your reservations", response.content)
        self.assertIn(b"Usertest", response.content)
        self.assertIn(b"Dec. 31, 2024", response.content)
        self.assertIn(b"12:00", response.content)
        self.assertIn(b"4", response.content)


        """
        Tests to see if the add reservation page renders.
        Tests to see if information can be submitted through the add reservation page.
        Tests to see if the edit reservation page renders.
        Tests to see if information can be submitted through the add reservation page.

        """