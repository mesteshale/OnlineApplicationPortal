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
        fields = ['id', 'user', 'application_info', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'user': {'required': False},
            'application_info': {'required': True}
        }

    def create(self, validated_data):
        print(f"Creating program selection with data: {validated_data}")
        try:
            # Get the current user from the request
            request = self.context.get('request')
            print(f"Request: {request}")
            print(f"Request data: {request.data if request else 'No request'}")

            user = request.user if request else validated_data.get('user')
            print(f"User: {user}")

            if not user:
                print("User is required but not provided")
                raise serializers.ValidationError("User is required")

            # Set the user in the validated data
            validated_data['user'] = user

            # Check if application_info is provided
            if 'application_info' not in validated_data:
                print("Application info is required but not provided")
                raise serializers.ValidationError({"application_info": ["This field is required."]})

            print(f"Updated validated_data: {validated_data}")

            # Check if the user already has a program selection record
            try:
                existing_selection = ApplicantProgramSelection.objects.get(user=user)
                print(f"User already has a program selection record with ID: {existing_selection.id}")

                # Update the existing record
                for key, value in validated_data.items():
                    print(f"Setting {key} = {value}")
                    setattr(existing_selection, key, value)
                existing_selection.save()
                print(f"Updated existing program selection record")
                return existing_selection
            except ApplicantProgramSelection.DoesNotExist:
                # Create a new record
                print("No existing record found, creating new one")
                instance = super().create(validated_data)
                print(f"Successfully created new program selection record with ID: {instance.id}")
                return instance
        except Exception as e:
            print(f"Error in program selection serializer create method: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

class ApplicantDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantDocumentation
        fields = ['id', 'user', 'degree', 'sponsorship', 'student_copy', 'recommendation', 'costsharing', 'publication', 'conceptnote', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'user': {'required': False},
            'degree': {'required': False},
            'sponsorship': {'required': False},
            'student_copy': {'required': False},
            'recommendation': {'required': False},
            'costsharing': {'required': False},
            'publication': {'required': False},
            'conceptnote': {'required': False}
        }

    def create(self, validated_data):
        print(f"Creating documentation with data: {validated_data}")
        try:
            # Get the current user from the request
            request = self.context.get('request')
            print(f"Request: {request}")

            user = request.user if request else validated_data.get('user')
            print(f"User: {user}")

            if not user:
                print("User is required but not provided")
                raise serializers.ValidationError("User is required")

            # Set the user in the validated data
            validated_data['user'] = user

            # Create a new record
            instance = super().create(validated_data)
            print(f"Successfully created new documentation record with ID: {instance.id}")
            return instance
        except Exception as e:
            print(f"Error in documentation serializer create method: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

class ApplicantPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantPayment
        fields = ['id', 'user', 'payment_amount', 'payment_status', 'payment_method', 'telebirr_id', 'transaction_id', 'payment_date', 'payment_time', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'user': {'required': False}
        }

    def create(self, validated_data):
        print(f"Creating payment with data: {validated_data}")
        try:
            # Get the current user from the request
            request = self.context.get('request')
            print(f"Request: {request}")

            user = request.user if request else validated_data.get('user')
            print(f"User: {user}")

            if not user:
                print("User is required but not provided")
                raise serializers.ValidationError("User is required")

            # Set the user in the validated data
            validated_data['user'] = user

            # Create a new record
            instance = super().create(validated_data)
            print(f"Successfully created new payment record with ID: {instance.id}")
            return instance
        except Exception as e:
            print(f"Error in payment serializer create method: {str(e)}")
            import traceback
            traceback.print_exc()
            raise