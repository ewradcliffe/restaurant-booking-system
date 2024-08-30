from django.shortcuts import render
from .models import Menu


# Create your views here.

def menu(request):
    """
    Renders the menu to the page
    """
    queryset = Menu.objects.all().values()

    """Create a list of all menu_entry_types with entries in th database"""
    menu_heading = [d.get('menu_entry_type', None) for d in queryset]

    """Convert to dictionary and back to list to remove duplicates."""
    menu_heading = list(dict.fromkeys(menu_heading))

    context = {
        'menu_heading': menu_heading,
        'menu_list': queryset
    }

    return render(
        request, 
        "menu/menu.html",
        context
    )   
    
    