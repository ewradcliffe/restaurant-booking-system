from . import views
from django.urls import path

urlpatterns = [
    path('', views.index.as_view(), name='index-urls'),
    path('reservations/', views.ReservationList.as_view(), name='reservations-urls'),
    path('add/', views.add_reservation, name='add-reservation'),
]

