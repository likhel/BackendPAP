from rest_framework import serializers
from .models import *
# from django.contrib.auth import get_user_model

class AdopterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdopterProfile
        fields = '__all__'

class AdoptionApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionApplication
        fields = '__all__'

class AdopterReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdopterReference
        fields = '__all__'