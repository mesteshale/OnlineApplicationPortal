from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import AdmissionType
from .serializers import AdmissionTypeSerializer

# List and Create view for AdmissionType (GET, POST)
class AdmissionTypeList(generics.ListCreateAPIView):
    serializer_class = AdmissionTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AdmissionType.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for AdmissionType (DELETE)
class AdmissionTypeDelete(generics.DestroyAPIView):
    serializer_class = AdmissionTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AdmissionType.objects.all()

# Retrieve and Update view for AdmissionType (GET, PUT)
class AdmissionTypeDetail(generics.RetrieveUpdateAPIView):
    serializer_class = AdmissionTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AdmissionType.objects.all()
