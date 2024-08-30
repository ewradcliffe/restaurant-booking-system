from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MENU_TYPE = (
    ('Starter', 'Starter'),
    ('Main', 'Main'),
    ('Dessert', 'Dessert'),
    ('Drinks', 'Drinks'),
)

class Menu(models.Model):
    """
    Class to manage menu entries.
    """
    menu_entry_type = models.CharField(max_length=10, choices=MENU_TYPE)
    menu_entry_name = models.CharField(max_length=50)
    menu_entry_description = models.TextField(max_length=100)
    menu_entry_price = models.DecimalField(max_digits=5, decimal_places=2)
    menu_entry_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        """
        Groups menu entries by type.
        """
        ordering = ["menu_entry_type"]

    def __str__(self):
        """
        Displays menu entry details.
        """
        return f"{self.menu_entry_type} | {self.menu_entry_name} | {self.menu_entry_price} |"
