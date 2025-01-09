from django.contrib import admin
from .models import *

# Register your models here.

class PetDetails(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'breed', 'gender', 'category', 'sterilization']
    search_fields = ['name']

admin.site.register(Pet, PetDetails)
admin.site.register(PetCategory)