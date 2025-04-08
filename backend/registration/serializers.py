from rest_framework import serializers
from .models import (
    ApplicantInformation,
    ApplicantGAT,
    ApplicantProgramSelection,
    ApplicantDocumentation,
    ApplicantPayment
)

class ApplicantInformationSerializer(serializers.ModelSerializer):
    # Add first_name and last_name from the User model
    first_name = serializers.CharField(source='author.first_name', read_only=True)
    last_name = serializers.CharField(source='author.last_name', read_only=True)

    # Use DateField with input formats
    dob = serializers.DateField(input_formats=['%Y-%m-%d', 'iso-8601'])

    def create(self, validated_data):
        print(f"Creating ApplicantInformation with data: {validated_data}")
        try:
            instance = super().create(validated_data)
            print(f"Successfully created instance: {instance}")
            return instance
        except Exception as e:
            print(f"Error in serializer create method: {str(e)}")
            raise

    class Meta:
        model = ApplicantInformation
        fields = ['id', 'author', 'first_name', 'last_name', 'grandfather_name', 'gender', 'dob', 'mobile', 'sponsorship',
                 'ug_university', 'ug_field_of_study', 'ug_CGPA',
                 'pg_university', 'pg_field_of_study', 'pg_CGPA',
                 'application_num', 'registrar_off_status', 'reg_approved_by',
                 'department_status', 'dep_approved_by', 'remark',
                 'payment_status', 'telebirr_id', 'created_at', 'updated_at']
        read_only_fields = ['author', 'application_num', 'created_at', 'updated_at']

    def validate_dob(self, value):
        """Validate that the date of birth is in the past"""
        import datetime
        if value > datetime.date.today():
            raise serializers.ValidationError("Date of birth must be in the past")
        return value

    def validate_ug_CGPA(self, value):
        """Validate that the CGPA is between 0 and 4.0"""
        if value < 0 or value > 4.0:
            raise serializers.ValidationError("CGPA must be between 0 and 4.0")
        return value

    def validate_pg_CGPA(self, value):
        """Validate that the CGPA is between 0 and 4.0 if provided"""
        if value is not None and (value < 0 or value > 4.0):
            raise serializers.ValidationError("CGPA must be between 0 and 4.0")
        return value

class ApplicantGATSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantGAT
        fields = ['id', 'user', 'GAT_No', 'GAT_Result']
        read_only_fields = ['user']

    def create(self, validated_data):
        print(f"Creating ApplicantGAT with data: {validated_data}")
        try:
            # Get the current user from the context
            user = self.context['request'].user
            validated_data['user'] = user

            # Check if the user already has a GAT record
            try:
                existing_gat = ApplicantGAT.objects.get(user=user)
                print(f"User already has a GAT record with ID: {existing_gat.id}")

                # Update the existing record
                for key, value in validated_data.items():
                    setattr(existing_gat, key, value)
                existing_gat.save()
                print(f"Updated existing GAT record")
                return existing_gat
            except ApplicantGAT.DoesNotExist:
                # Create a new record
                instance = super().create(validated_data)
                print(f"Successfully created new GAT record with ID: {instance.id}")
                return instance
        except Exception as e:
            print(f"Error in GAT serializer create method: {str(e)}")
            raise

class ApplicantProgramSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantProgramSelection
        fields = '__all__'

class ApplicantDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantDocumentation
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ApplicantPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantPayment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']