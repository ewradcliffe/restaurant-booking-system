from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
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
    Function to delete reservations.
    Adapted from https://www.w3schools.com/django/django_delete_members.php
    """
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    return render(
            request, 
            "reservations/reservation_confirmed.html",
        )


def edit_reservation(request, id):
    """
    Function to edit reservations.
    Adapted from https://www.w3schools.com/django/django_update_record.php
    """
    reservation = Reservation.objects.get(id=id)
    template = loader.get_template('reservations/edit_reservation.html')
    context = {
        'reservation': reservation,
    }
    return HttpResponse(template.render(context, request))

def update_reservation(request, id):
    """
    Function to post updated reservation data.
    Adapted from https://www.w3schools.com/django/django_update_record.php
    """
    reservation_name = request.POST['reservation_name']
    reservation_date = request.POST['reservation_date']
    reservation_time = request.POST['reservation_time']
    number_of_guests = request.POST['number_of_guests']
    reservation = Reservation.objects.get(id=id)
    reservation.reservation_name = reservation_name
    reservation.reservation_date = reservation_date
    reservation.reservation_time = reservation_time
    reservation.number_of_guests = number_of_guests
    reservation.save()
    return render(
        request, 
        "reservations/reservation_confirmed.html",
    )

