from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        # Get the username and password from the request
        username = attrs.get('username')
        password = attrs.get('password')

        print(f"Login attempt with username: {username}")

        if username and password:
            # First try to authenticate with username
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # If that fails, try to find a user with this email and authenticate with their username
            if not user:
                print(f"Authentication failed with username: {username}")
                try:
                    # Try to find a user with this email
                    user_obj = User.objects.filter(email=username).first()
                    if user_obj:
                        print(f"Found user with email {username}, trying with username: {user_obj.username}")
                        # Try to authenticate with the username
                        user = authenticate(request=self.context.get('request'),
                                            username=user_obj.username, password=password)
                except Exception as e:
                    print(f"Error looking up user by email: {str(e)}")

            # If authentication still fails, raise an error
            if not user:
                from rest_framework import serializers
                print("Authentication failed completely")
                raise serializers.ValidationError(
                    'No active account found with the given credentials'
                )
            else:
                print(f"Authentication successful for user: {user.username}")
        else:
            from rest_framework import serializers
            print("Missing username or password")
            raise serializers.ValidationError(
                'Must include "username" and "password".'
            )

        # If authentication is successful, proceed with token generation
        data = {}
        refresh = self.get_token(user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
