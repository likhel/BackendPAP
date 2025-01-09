from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class ContactSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = '__all__'