from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ApplicationInformation
from .serializers import ApplicationInformationSerializer

# Create your views here.

# Filter view for ApplicationInformation
class ApplicationInformationFilter(generics.ListAPIView):
    serializer_class = ApplicationInformationSerializer
    permission_classes = [AllowAny]  # Allow any user to search

    def get_queryset(self):
        # Start with all active application information records
        queryset = ApplicationInformation.objects.filter(status=True)

        # Print the total number of records for debugging
        print(f"Total ApplicationInformation records: {queryset.count()}")

        # Get query parameters
        college_id = self.request.query_params.get('college')
        department_id = self.request.query_params.get('department')
        program_id = self.request.query_params.get('program')
        admission_type_id = self.request.query_params.get('admission_type')

        # Print the filter parameters for debugging
        print(f"Filter parameters: college={college_id}, department={department_id}, program={program_id}, admission_type={admission_type_id}")

        # If no filters are provided, return all records
        if not any([college_id, department_id, program_id, admission_type_id]):
            print("No filters provided, returning all records")
            return queryset

        # If all filters are '0' (meaning 'All'), return all records
        if (college_id == '0' or not college_id) and \
           (department_id == '0' or not department_id) and \
           (program_id == '0' or not program_id) and \
           (admission_type_id == '0' or not admission_type_id):
            print("All filters are 'All', returning all records")
            return queryset

        # Apply filters if parameters are provided
        if college_id and college_id != '0':
            try:
                # Try to filter by college_id
                queryset = queryset.filter(college_id=int(college_id))
                print(f"Filtered by college_id={college_id}, remaining records: {queryset.count()}")
            except (ValueError, Exception) as e:
                print(f"Error filtering by college_id: {e}")
                # If there's an error, don't apply this filter
                pass

        if department_id and department_id != '0':
            try:
                # Try to filter by department_id
                queryset = queryset.filter(department_id=int(department_id))
                print(f"Filtered by department_id={department_id}, remaining records: {queryset.count()}")
            except (ValueError, Exception) as e:
                print(f"Error filtering by department_id: {e}")
                # If there's an error, don't apply this filter
                pass

        if program_id and program_id != '0':
            try:
                # Try to filter by program_id
                queryset = queryset.filter(program_id=int(program_id))
                print(f"Filtered by program_id={program_id}, remaining records: {queryset.count()}")
            except (ValueError, Exception) as e:
                print(f"Error filtering by program_id: {e}")
                # If there's an error, don't apply this filter
                pass

        if admission_type_id and admission_type_id != '0':
            try:
                # Check if admission_type_id is a string like 'Regular', 'Extension', etc.
                if admission_type_id in ['Regular', 'Extension', 'Distance']:
                    # If it's a name, filter by the name
                    queryset = queryset.filter(admission_type__name=admission_type_id)
                    print(f"Filtered by admission_type_name={admission_type_id}, remaining records: {queryset.count()}")
                else:
                    try:
                        # Try to use it as an ID
                        queryset = queryset.filter(admission_type_id=int(admission_type_id))
                        print(f"Filtered by admission_type_id={admission_type_id}, remaining records: {queryset.count()}")
                    except ValueError:
                        # If it's not a valid ID, don't apply this filter
                        print(f"Invalid admission_type_id: {admission_type_id}, skipping this filter")
                        pass
            except Exception as e:
                print(f"Error filtering by admission_type_id: {e}")
                # If there's an error, don't apply this filter
                pass

        # If no records match the filters, return an empty queryset
        if queryset.count() == 0:
            print("No records match the filters")

        return queryset

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