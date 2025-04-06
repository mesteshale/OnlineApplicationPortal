from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ApplicationInformation
from .serializers import ApplicationInformationSerializer

# Create your views here.

# List and Create view for ApplicationInformation (GET, POST)
class ApplicationInformationList(generics.ListCreateAPIView):
    serializer_class = ApplicationInformationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicationInformation.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for AdmissionType (DELETE)
class ApplicationInformationDelete(generics.DestroyAPIView):
    serializer_class = ApplicationInformationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicationInformation.objects.all()
    
# Retrieve and Update view for AdmissionType (GET, PUT)
class ApplicationInformationDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ApplicationInformationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicationInformation.objects.all()