from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import StudyProgram
from .serializers import StudyProgramSerializer

# Create your views here.
# List and Create view for StudyProgram (GET, POST)
class StudyProgramList(generics.ListCreateAPIView):
    serializer_class = StudyProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyProgram.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for StudyProgram (DELETE)
class StudyProgramDelete(generics.DestroyAPIView):
    serializer_class = StudyProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyProgram.objects.all()

# Retrieve and Update view for StudyProgram (GET, PUT)
class StudyProgramDetail(generics.RetrieveUpdateAPIView):
    serializer_class = StudyProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyProgram.objects.all()