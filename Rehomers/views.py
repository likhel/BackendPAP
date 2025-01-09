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

class RehomerApplicationCreateView(generics.CreateAPIView):
    serializer_class = RehomerApplicationSerializer
    queryset = RehomerApplication.objects.all()

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
