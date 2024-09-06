from django.contrib import admin
from .models import Menu
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('menu_entry_type', 'menu_entry_name', 'menu_entry_price')
    summernote_fields = ('menu_entry_description',)
