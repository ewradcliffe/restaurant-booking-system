from django.contrib import admin
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('reservation_name', 'reservation_date', 'reservation_time', 'number_of_guests')
    search_fields = ['reservation_name']
    list_filter = ('reservation_date', 'reservation_time')
