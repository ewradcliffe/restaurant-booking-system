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
        self.assertTrue(self.client.login(username='username', password='password123!'))
        response = self.client.get(reverse('reservations-urls'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"You are not logged in", response.content)
        self.assertIn(b"Your reservations", response.content)
        self.assertIn(b"Usertest", response.content)
        self.assertIn(b"Dec. 31, 2024", response.content)
        self.assertIn(b"12:00", response.content)
        self.assertIn(b"4", response.content)

    
    def test_render_add_reservation_page(self):
        """
        Test to see if the add reservation page is rendered.
        """
        self.client.login(username='username', password='password123!')
        response = self.client.get(reverse('add-reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Please log in to make a reservation", response.content)
       

    def test_render_edit_reservation_page(self):
        """
        Test to see if the edit reservation page works.
        """
        self.client.login(username='username', password='password123!')
        response = self.client.get(reverse('edit-reservation', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Please log in to make a reservation", response.content)
        self.assertIn(b"Usertest", response.content)
        self.assertIn(b"2024-12-31", response.content)
        self.assertIn(b"12:00", response.content)
        

    def test_render_delete_reservation_page(self):
        """
        Test to see if the delete reservation page renders.
        """
        self.client.login(username='username', password='password123!')
        response = self.client.get(reverse('delete-reservation', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Usertest", response.content)
        self.assertIn(b"Dec. 31, 2024", response.content)
        self.assertIn(b"12:00", response.content)
        self.assertIn(b"4", response.content)


    def test_successful_add_reservation(self):
        """
        Test for making a reservation
        """
        self.client.login(username='username', password='password123!')
        reservation = {
            'reservation_name': 'Usertest', 
            'reservation_date': '2024-12-31', 
            'reservation_time': '13:00', 
            'number_of_guests':'2'  
        }
        response = self.client.post(reverse('add-reservation'), reservation)
        
        """Tests to see if we are redirected after submitting"""
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('reservations-urls'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your reservation was successfully made!', response.content)


    def test_successful_edit_reservation(self):
        """
        Test for editing a reservation
        In this case I am updating the number of guests from 4 to 2.
        """
        self.client.login(username='username', password='password123!')
        reservation = {
            'reservation_name': 'Usertest', 
            'reservation_date': '2024-12-31', 
            'reservation_time': '12:00', 
            'number_of_guests':'2'  
        }

        response = self.client.post(reverse('edit-reservation', args=['1']), reservation)
        """Tests to see if we are redirected after submitting"""
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('reservations-urls'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Usertest", response.content)
        self.assertIn(b"Dec. 31, 2024", response.content)
        self.assertIn(b"12:00", response.content)
        self.assertIn(b"2", response.content)
    
        
    def test_successful_delete_reservation(self):
        """
        Test for deleting a reservation
        """
        self.client.login(username='username', password='password123!')
        reservation = {
            'reservation_name': 'Usertest', 
            'reservation_date': '2024-12-31', 
            'reservation_time': '13:00', 
            'number_of_guests':'2'  
        }
        response = self.client.post(reverse('confirm-delete-reservation', args=['1']), reservation)

        """Tests to see if we are redirected after deleting"""
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('reservations-urls'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Usertest", response.content)
        self.assertNotIn(b"Dec. 31, 2024", response.content)
        self.assertNotIn(b"13:00", response.content)


