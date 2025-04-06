from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,CollegeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from setups.college.models import College

# List and Create view for College (GET, POST)
class CollegeList(generics.ListCreateAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return College.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for College (DELETE)
class CollegeDelete(generics.DestroyAPIView): 
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]     

    def get_queryset(self):
        return College.objects.all()   
    
# Retrieve and Update view for a single College (GET, PUT)
class CollegeDetail(generics.RetrieveUpdateAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return College.objects.all()

# #####################################################################################################
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



