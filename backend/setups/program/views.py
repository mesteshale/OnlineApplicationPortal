from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Program
from .serializers import ProgramSerializer
# Create your views here.

class ProgramList(generics.ListCreateAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Program.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
class ProgramDelete(generics.DestroyAPIView): 
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]     

    def get_queryset(self):
        return Program.objects.all()
class ProgramDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Program.objects.all()
    