from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
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

# Public list view for Program (GET)
class PublicProgramList(generics.ListAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['program_code', 'program_name']

    def get_queryset(self):
        return Program.objects.all()
