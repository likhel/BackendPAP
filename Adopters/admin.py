from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(AdopterProfile)
admin.site.register(AdoptionApplication)
admin.site.register(AdopterReference)