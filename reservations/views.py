from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Reservation


# Create your views here.
class index(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/index.html"

class ReservationList(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/reservation.html"



    
