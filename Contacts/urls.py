from django.urls import path, include
from .views import *

urlpatterns = [
    path("contacts", ContactView.as_view(), name='contacts'),
]
