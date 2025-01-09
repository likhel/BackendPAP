from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class RehomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehomerProfile
        fields = '__all__'

class RehomerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehomerApplication
        fields = '__all__'
        
# class RehomerReferenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RehomerReference
#         fields = '__all__'