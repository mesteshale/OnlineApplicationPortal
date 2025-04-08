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
        # Filter by the current user
        return ApplicantInformation.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        # Set the author to the current user
        print(f"Creating ApplicantInformation for user: {self.request.user}")
        print(f"Serializer data: {serializer.validated_data}")

        # Check if the user already has an ApplicantInformation record
        try:
            existing_info = ApplicantInformation.objects.get(author=self.request.user)
            print(f"User already has an ApplicantInformation record with ID: {existing_info.id}")

            # Update the existing record instead of creating a new one
            for key, value in serializer.validated_data.items():
                setattr(existing_info, key, value)
            existing_info.save()
            print(f"Updated existing ApplicantInformation record")
            return existing_info
        except ApplicantInformation.DoesNotExist:
            # Create a new record if one doesn't exist
            try:
                instance = serializer.save(author=self.request.user)
                print(f"Successfully created new ApplicantInformation with ID: {instance.id}")
                return instance
            except Exception as e:
                print(f"Error creating ApplicantInformation: {str(e)}")
                raise

class ApplicantInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantInformationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantInformation.objects.filter(author=self.request.user)

# ApplicantGAT views
class ApplicantGATList(generics.ListCreateAPIView):
    serializer_class = ApplicantGATSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantGAT.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user to the current user
        print(f"Creating ApplicantGAT for user: {self.request.user}")
        print(f"Serializer data: {serializer.validated_data}")
        try:
            instance = serializer.save(user=self.request.user)
            print(f"Successfully created ApplicantGAT with ID: {instance.id}")
        except Exception as e:
            print(f"Error creating ApplicantGAT: {str(e)}")
            raise

class ApplicantGATDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantGATSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantGAT.objects.filter(user=self.request.user)

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
