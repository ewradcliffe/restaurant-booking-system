from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Reservation



# Create your views here.
class index(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/index.html"



class ReservationList(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/reservation.html"


class AddReservation(CreateView):
    model = Reservation
    template_name = "reservations/add_reservation.html"
    fields = ('reservation_name', 'reservation_email', 'reservation_phone_number', 'reservation_date', 'reservation_time', 'number_of_guests', )
    





    
