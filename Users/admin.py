from django.contrib import admin
from .models import *

# Register your models here.
class CustomUsersDetails(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role', 'address', 'contact_number']
    search_fields = ['username'] 

admin.site.register(CustomUsers, CustomUsersDetails)