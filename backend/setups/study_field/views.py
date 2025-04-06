from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import StudyField
from .serializers import StudyFieldSerializer

# Create your views here.
# List and Create view for StudyField (GET, POST)
class StudyFieldList(generics.ListCreateAPIView):
    serializer_class = StudyFieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyField.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
# Delete view for StudyField (DELETE)
class StudyFieldDelete(generics.DestroyAPIView):
    serializer_class = StudyFieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyField.objects.all()
# Retrieve and Update view for StudyField (GET, PUT)
class StudyFieldDetail(generics.RetrieveUpdateAPIView):
    serializer_class = StudyFieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyField.objects.all()