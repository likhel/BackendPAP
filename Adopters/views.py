from django.shortcuts import render
from rest_framework import viewsets, generics
from .serialization import *
from .models import *

# Create your views here.

#For Adopter Profiles
class AdopterProfileView(generics.ListAPIView):
    queryset = AdopterProfile.objects.all()
    serializer_class = AdopterProfileSerializer

class AdopterProfileCreateView(generics.CreateAPIView):
    queryset = AdopterProfile.objects.all()
    serializer_class = AdopterProfileSerializer

class AdopterProfileRetrieveView(generics.RetrieveAPIView):
    queryset = AdopterProfile.objects.all()
    serializer_class = AdopterProfileSerializer
class AdopterProfileUpdateView(generics.UpdateAPIView):
    queryset = AdopterProfile.objects.all()
    serializer_class = AdopterProfileSerializer

class AdopterProfileDeleteView(generics.DestroyAPIView):
    queryset = AdopterProfile.objects.all()
    serializer_class = AdopterProfileSerializer

#For Adoption Applications

class AdoptionApplicationView(generics.ListAPIView):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer

class AdoptionApplicationCreateView(generics.CreateAPIView):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer

class AdoptionApplicationUpdateView(generics.UpdateAPIView):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer

class AdoptionApplicationDeleteView(generics.DestroyAPIView):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer

#For Adopter References

class AdopterReferenceView(generics.ListAPIView):
    queryset = AdopterReference.objects.all()
    serializer_class = AdopterReferenceSerializer





