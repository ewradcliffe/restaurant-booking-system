from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu.as_view(), name='menu'),
]