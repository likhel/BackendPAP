from django.contrib import admin
from .models import *

class ContactDetails(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    search_fields = ['name']
    
# Register your models here.

admin.site.register(Contact, ContactDetails)