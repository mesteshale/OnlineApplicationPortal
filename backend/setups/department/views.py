from django.shortcuts import render
from setups.department.models import Department
from rest_framework import generics
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
 
# List and Create view for Department (GET, POST)
class DepartmentList(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for Department (DELETE)
class DepartmentDelete(generics.DestroyAPIView): 
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]     

    def get_queryset(self):
        return Department.objects.all()   
    
#Retrieve and Update view for a single College (GET, PUT)
class DepartmentDetail(generics.RetrieveUpdateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.all() 