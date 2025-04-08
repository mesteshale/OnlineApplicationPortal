from rest_framework import serializers
from django.contrib.auth.models import User
from .models import College


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
       model = College
       fields = ['id', 'name', 'description', 'created_at', 'updated_at']


# #################################################################################################
# User Serializers

class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer for returning user details to the client"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = fields

class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        # Define extra_kwargs to make password1 and password2 write-only
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
            'email': {'required': True},  # Ensure email is required
            'first_name': {'required': False},  # Make first_name optional
            'last_name': {'required': False}   # Make last_name optional
        }

    def validate(self, data):
        """
        Check that the two passwords match.
        """
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")

        # Ensure email is valid and not empty
        email = data.get('email')
        if not email:
            raise serializers.ValidationError("Email is required.")

        return data

    def create(self, validated_data):
        """
        Create a new user and return it.
        """
        # Remove password2 from validated data as it's not needed for user creation
        validated_data.pop('password2', None)

        # Extract password1 for user creation (create_user expects 'password')
        password = validated_data.pop('password1')

        # Extract first_name and last_name if present
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')

        # Create the user using create_user method (this handles password hashing)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )

        # Set first_name and last_name separately
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return user
