from django.contrib import admin
from .models import *

# Register your models here.

class RehomerProfileDetails(admin.ModelAdmin):
    list_display = ['id', 'user', 'rehome_history']
    search_fields = ['name']
                     
admin.site.register(RehomerProfile, RehomerProfileDetails)