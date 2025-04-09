from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
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
        # Filter by the current user
        return ApplicantProgramSelection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(f"Creating program selection for user: {self.request.user}")
        print(f"Request data: {self.request.data}")
        print(f"Serializer validated data: {serializer.validated_data}")

        try:
            # Check if the user already has a program selection record
            try:
                existing_selection = ApplicantProgramSelection.objects.get(user=self.request.user)
                print(f"User already has a program selection record with ID: {existing_selection.id}")

                # Update the existing record
                for key, value in serializer.validated_data.items():
                    print(f"Setting {key} = {value}")
                    setattr(existing_selection, key, value)
                existing_selection.save()
                print(f"Updated existing program selection record")
                return existing_selection
            except ApplicantProgramSelection.DoesNotExist:
                # Create a new record
                print("No existing record found, creating new one")
                instance = serializer.save(user=self.request.user)
                print(f"Successfully created new program selection record with ID: {instance.id}")
                return instance
        except Exception as e:
            print(f"Error in program selection view: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

class ApplicantProgramSelectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantProgramSelectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantProgramSelection.objects.filter(user=self.request.user)

# ApplicantDocumentation views
class ApplicantDocumentationList(generics.ListCreateAPIView):
    serializer_class = ApplicantDocumentationSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantDocumentation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(f"Creating documentation for user: {self.request.user}")
        try:
            # Check if the user already has a documentation record
            try:
                existing_doc = ApplicantDocumentation.objects.get(user=self.request.user)
                print(f"User already has a documentation record with ID: {existing_doc.id}")

                # Update the existing record
                for key, value in serializer.validated_data.items():
                    if value is not None:  # Only update if a new file is provided
                        print(f"Setting {key} = {value}")
                        setattr(existing_doc, key, value)
                existing_doc.save()
                print(f"Updated existing documentation record")
                return existing_doc
            except ApplicantDocumentation.DoesNotExist:
                # Create a new record
                print("No existing record found, creating new one")
                instance = serializer.save(user=self.request.user)
                print(f"Successfully created new documentation record with ID: {instance.id}")
                return instance
        except Exception as e:
            print(f"Error in documentation view: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

class ApplicantDocumentationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantDocumentationSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantDocumentation.objects.filter(user=self.request.user)

# ApplicantPayment views
class ApplicantPaymentList(generics.ListCreateAPIView):
    serializer_class = ApplicantPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantPayment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(f"Creating payment for user: {self.request.user}")
        try:
            # Check if the user already has a payment record
            try:
                existing_payment = ApplicantPayment.objects.get(user=self.request.user)
                print(f"User already has a payment record with ID: {existing_payment.id}")

                # Update the existing record
                for key, value in serializer.validated_data.items():
                    print(f"Setting {key} = {value}")
                    setattr(existing_payment, key, value)
                existing_payment.save()
                print(f"Updated existing payment record")
                return existing_payment
            except ApplicantPayment.DoesNotExist:
                # Create a new record
                print("No existing record found, creating new one")
                instance = serializer.save(user=self.request.user)
                print(f"Successfully created new payment record with ID: {instance.id}")
                return instance
        except Exception as e:
            print(f"Error in payment view: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

class ApplicantPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the current user for security
        return ApplicantPayment.objects.filter(user=self.request.user)
