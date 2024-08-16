from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.template import loader
from django.views import generic
from django.contrib import messages
from .models import Reservation, User
from .forms import ReservationForm
from datetime import datetime


# Create your views here.
class index(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/index.html"


class ReservationList(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservations/reservation.html"


def check_time(date_choice, time_choice, datetime):
    "Function to check booked dates and times are in the future."
    booking_time = datetime.strptime(date_choice+' '+time_choice, '%Y-%m-%d %H:%M')
    
    if booking_time > datetime.now():
        return True
    else:
        return False


def add_reservation(request):
    """
    Renders reservation form to screen.
    """
    reservation_form = ReservationForm()

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            """
            Check if date and time are in the future.
            """
            date = reservation.reservation_date
            time = reservation.reservation_time
            datetime_choice_valid = check_time(str(date), time, datetime)
            if datetime_choice_valid:
                """
                Adds user details to reservation.
                """
                reservation.reservation_booked_by = request.user
                reservation.reservation_email = request.user.email
                reservation.reservation_created_on = datetime.now()
                reservation.save()
                messages.add_message(request, messages.SUCCESS,
                'Your reservation was successfully made!')
                return HttpResponseRedirect(reverse('reservations-urls'))

            else:
                messages.add_message(request, messages.SUCCESS,
                'You entered a time in the past. Please enter a later time.')

    return render(
        request, 
        "reservations/add_reservation.html", {
            "reservation_form": reservation_form,
        }
    )

    
def delete_reservation(request, id):
    """
    Function to check user wants to delete reservation.
    """
    reservation = get_object_or_404(Reservation, id=id)
    context = {
        'reservation': reservation,
    }

    return render(
        request, 
        "reservations/delete_reservation.html",
        context
    )   
    
       
def confirm_delete_reservation(request, id):
    """
    Function to delete reservation.
    Adapted from https://www.w3schools.com/django/django_delete_members.php
    """
    reservation = Reservation.objects.get(id=id)    
    reservation.delete()
    messages.add_message(request, messages.SUCCESS,
    'Your reservation has been deleted.')
    return HttpResponseRedirect(reverse('reservations-urls'))


def edit_reservation(request, id):
    """
    Function to edit reservations.
    """
    reservation = get_object_or_404(Reservation, id=id)

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST, instance=reservation)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            """
            Check if date and time are in the future.
            """
            date = reservation.reservation_date
            time = reservation.reservation_time
            datetime_choice_valid = check_time(str(date), time, datetime)
            if datetime_choice_valid:
                
                reservation.reservation_booked_by = request.user
                reservation.reservation_email = request.user.email
                reservation.save()
                messages.add_message(request, messages.SUCCESS,
                'Your reservation has been updated!')
                return HttpResponseRedirect(reverse('reservations-urls'))

            else:
                messages.add_message(request, messages.SUCCESS,
                'You entered a time in the past. Please enter a later time.')
    else:
        reservation_form = ReservationForm(instance=reservation)

    context = {
        "reservation_form": reservation_form,
        'reservation': reservation,
    }

    return render(
        request, 
        "reservations/edit_reservation.html",
        context
    )   
