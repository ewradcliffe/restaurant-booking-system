from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Reservation, User
from .forms import ReservationForm


# Create your views here.
class index(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/index.html"


class ReservationList(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/reservation.html"


def add_reservation(request):
    """
    Renders reservation form to screen.
    """
    reservation_form = ReservationForm()

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.reservation_booked_by = request.user
            reservation.reservation_email = request.user.email
            reservation.save()
            return render(
            request, 
            "reservations/reservation_confirmed.html",
        )

    return render(
        request, 
        "reservations/add_reservation.html", {
            "reservation_form": reservation_form,
        }
    )

    
def delete_reservation(request, id):
    """
    Function to delete reservations
    """
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    return render(
            request, 
            "reservations/reservation_confirmed.html",
        )

