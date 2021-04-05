from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact Sign Up"""
    list_display = ("email", "date",)
    list_display_links = ("email", )
    save_on_top = True