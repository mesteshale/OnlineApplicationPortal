from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import RegistrationPeriod
from .serializers import RegistrationPeriodSerializer

# Create your views here.

# List and Create view for RegistrationPeriod (GET, POST)
class RegistrationPeriodList(generics.ListCreateAPIView):
    serializer_class = RegistrationPeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RegistrationPeriod.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for RegistrationPeriod (DELETE)
class RegistrationPeriodDelete(generics.DestroyAPIView):
    serializer_class = RegistrationPeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RegistrationPeriod.objects.all() 

# Retrieve and Update view for RegistrationPeriod (GET, PUT)
class RegistrationPeriodDetail(generics.RetrieveUpdateAPIView):
    serializer_class = RegistrationPeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RegistrationPeriod.objects.all()
    