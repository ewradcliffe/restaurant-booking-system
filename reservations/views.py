from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
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

    
    
    """
    reservation_booked_by = User

    class AddReservation(CreateView):

    model = Reservation
    template_name = "reservations/add_reservation.html"
    fields = ('reservation_name', 'reservation_email', 'reservation_phone_number', 'reservation_date', 'reservation_time', 'number_of_guests',)
    """







    
