from django.shortcuts import render
from .models import Menu


# Create your views here.

def menu(request):
    """
    Renders the menu to the page
    """
    queryset = Menu.objects.all().values()
    menu_heading = ('Starter', 'Main', 'Dessert', 'Drinks')

    context = {
        'menu_heading': menu_heading,
        'menu_list': queryset
    }

    return render(
        request, 
        "menu/menu.html",
        context
    )   
    
    