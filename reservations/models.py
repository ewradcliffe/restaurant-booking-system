from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

# reservation_time and number_of_guests code inspired by https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78


RESERVATION_TIME = (
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
   
)

NUMBER_OF_GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
)

class Reservation(models.Model):
    """
    Class to manage reservations.
    """
    reservation_name = models.CharField(max_length=60)
    reservation_email = models.EmailField(blank=True, null=True)
    reservation_phone_number = models.IntegerField(blank=True, null=True)
    reservation_date = models.DateField()
    reservation_time = models.CharField(choices=RESERVATION_TIME)
    number_of_guests = models.CharField(choices=NUMBER_OF_GUESTS)
    reservation_booked_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    reservation_created_on = models.DateTimeField(auto_now_add=True)
    reservation_updated_on = models.DateTimeField(auto_now=True)

    # NB I have not set an on delete on reservation_booked_by because I want staff
    # to be able to make reservations on the behalf of others.

    class Meta:
        """
        Orders reservations. Soonest reservations first."
        """
        ordering = ["reservation_date", "-reservation_time"]

    def __str__(self):
        """
        Displays most useful reservation information.
        """
        return f"{self.reservation_name} | {self.reservation_date} | {self.reservation_time} | {self.number_of_guests}"
