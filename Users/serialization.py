from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Ensure you're referencing CustomUsers
        fields = ['username', 'email', 'contact_number', 'password','role']  # Added contact_number
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data.get('role', 1)
           
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        # Check for existing email or username
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "A user with that email already exists."})
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "A user with that username already exists."})
        # if data.get('contact_number') and User.objects.filter(contact_number=data['contact_number']).exists():
        #     raise serializers.ValidationError({"contact_number": "This contact number is already in use."})
        
        return data