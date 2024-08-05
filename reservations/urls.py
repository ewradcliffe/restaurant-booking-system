from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationList.as_view(), name='reservations-urls'),
]

