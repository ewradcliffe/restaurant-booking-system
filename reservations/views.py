from django.shortcuts import render
from django.views import generic
from .models import Reservation


# Create your views here.

class ReservationList(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/index.html"
