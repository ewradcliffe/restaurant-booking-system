from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
#from .models import Menu

# Create your views here.

class menu(generic.ListView):
    """
    Renders the menu to the page
    """

    #queryset = Menu.objects.all()
    #template_name = "menu.html"
    