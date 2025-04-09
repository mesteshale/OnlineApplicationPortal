from django.shortcuts import render
from setups.department.models import Department
from rest_framework import generics, filters
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
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

#Retrieve and Update view for a single Department (GET, PUT)
class DepartmentDetail(generics.RetrieveUpdateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.all()

# Public list view for Department (GET)
class PublicDepartmentList(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Department.objects.all()
        college_id = self.request.query_params.get('college')
        if college_id:
            queryset = queryset.filter(college_id=college_id)
        return queryset