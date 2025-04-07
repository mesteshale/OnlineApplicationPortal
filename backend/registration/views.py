from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import (
    ApplicantInformation, 
    ApplicantGAT, 
    ApplicantProgramSelection, 
    ApplicantDocumentation,
    ApplicantPayment
)
from .serializers import (
    ApplicantInformationSerializer,
    ApplicantGATSerializer,
    ApplicantProgramSelectionSerializer,
    ApplicantDocumentationSerializer,
    ApplicantPaymentSerializer
)

# ApplicantInformation views
class ApplicantInformationList(generics.ListCreateAPIView):
    serializer_class = ApplicantInformationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicantInformation.objects.all()

class ApplicantInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantInformationSerializer
    permission_classes = [IsAuthenticated]
    queryset = ApplicantInformation.objects.all()

# ApplicantGAT views
class ApplicantGATList(generics.ListCreateAPIView):
    serializer_class = ApplicantGATSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicantGAT.objects.all()

class ApplicantGATDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantGATSerializer
    permission_classes = [IsAuthenticated]
    queryset = ApplicantGAT.objects.all()

# ApplicantProgramSelection views
class ApplicantProgramSelectionList(generics.ListCreateAPIView):
    serializer_class = ApplicantProgramSelectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicantProgramSelection.objects.all()

class ApplicantProgramSelectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantProgramSelectionSerializer
    permission_classes = [IsAuthenticated]
    queryset = ApplicantProgramSelection.objects.all()

# ApplicantDocumentation views
class ApplicantDocumentationList(generics.ListCreateAPIView):
    serializer_class = ApplicantDocumentationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicantDocumentation.objects.all()

class ApplicantDocumentationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantDocumentationSerializer
    permission_classes = [IsAuthenticated]
    queryset = ApplicantDocumentation.objects.all()

# ApplicantPayment views
class ApplicantPaymentList(generics.ListCreateAPIView):
    serializer_class = ApplicantPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApplicantPayment.objects.all()

class ApplicantPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantPaymentSerializer
    permission_classes = [IsAuthenticated]
    queryset = ApplicantPayment.objects.all()
