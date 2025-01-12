from django.shortcuts import render
from .serialization import *
from rest_framework import generics
from .models import *

# Create your views here.

#For Rehomer Profiles

class RehomerProfileView(generics.ListAPIView):
    serializer_class = RehomerProfileSerializer
    queryset = RehomerProfile.objects.all() 

class RehomerProfileCreateView(generics.CreateAPIView):
    serializer_class = RehomerProfileSerializer
    queryset = RehomerProfile.objects.all()

class RehomerProfileRetrieveView(generics.RetrieveAPIView):
    serializer_class = RehomerProfileSerializer
    queryset = RehomerProfile.objects.all()

class RehomerProfileUpdateView(generics.UpdateAPIView):
    serializer_class = RehomerProfileSerializer
    queryset = RehomerProfile.objects.all()

class RehomerProfileDeleteView(generics.DestroyAPIView):
    serializer_class = RehomerProfileSerializer
    queryset = RehomerProfile.objects.all()

#For Rehomer Applications

class RehomerApplicationView(generics.ListAPIView):
    serializer_class = RehomerApplicationSerializer
    queryset = RehomerApplication.objects.all()

from rest_framework.views import APIView
from Pets.models import Pet
from Rehomers.models import RehomerApplication
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status

class RehomerApplicationCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Get data from request
            data = request.data

            # Create a Pet instance
            pet = Pet.objects.create(
                category=data['pets']['petType'],
                
                name=data['aboutPet']['name'],
                age=data['aboutPet']['age'],
                breed=data['aboutPet']['breed'],
                size=data['aboutPet']['size'],
                pet_image=['aboutPet']['pet_image'],
                gender=data['aboutPet']['gender'],
                sterilization=data['aboutPet']['sterilization'],
                color=data['aboutPet']['color'],
                owned_time=data['aboutPet']['owned-time'],
                source=data['aboutPet']['getFrom'],  # Mapped to the "getFrom" field
                household_activity=data['petHousehold']['HouseholdActivity'],
                lives_with_other_pets=data['petHousehold']['SinglePet'],
                household_environment=data['petHousehold']['PetEnvironment'],
                behaviour=data['petType']['behaviour'],
                socialization_issues=data['petType']['socializationIssues']
            )

            # Fetch the user instance
            User = get_user_model()
            rehomer_user = User.objects.get(id=1)  # Replace 1 with the appropriate ID logic

            # Create the RehomerApplication
            rehomer = RehomerApplication.objects.create(pet=pet, rehomer=rehomer_user)

            # Return a valid response
            return Response({"RehomerAppid": rehomer.id}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Handle exceptions gracefully
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RehomerApplicationUpdateView(generics.UpdateAPIView):
    serializer_class = RehomerApplicationSerializer
    queryset = RehomerApplication.objects.all()

class RehomerApplicationDeleteView(generics.DestroyAPIView):
    serializer_class = RehomerApplicationSerializer
    queryset = RehomerApplication.objects.all()

#For Adopter References

# class RehomerReferenceView(generics.ListAPIView):
#     serializer_class = RehomerReferenceSerializer
#     queryset = RehomerReference.objects.all()
