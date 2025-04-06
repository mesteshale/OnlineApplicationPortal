from rest_framework import serializers
from .models import RegistrationPeriod
from django.utils import timezone
from datetime import datetime

class RegistrationPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationPeriod
        fields = ['id', 'name', 'open_date', 'close_date', 'created_at', 'is_active']

    def validate_open_date(self, value):
        """
        Ensure that the open_date is after the current date and time.
        """
        # Convert value to datetime if it is a string
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        
        # Make sure the open_date is timezone-aware
        if value.tzinfo is None:
            value = timezone.make_aware(value)

        if value <= timezone.now():
            raise serializers.ValidationError("The opening date must be after the current date and time.")
        return value

    def validate_close_date(self, value):
        """
        Ensure that the close_date is after the open_date.
        """
        # Convert value to datetime if it is a string
        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        # Make sure the close_date is timezone-aware
        if value.tzinfo is None:
            value = timezone.make_aware(value)

        open_date = self.initial_data.get('open_date')

        # Convert open_date to datetime if it is a string
        if isinstance(open_date, str):
            open_date = datetime.fromisoformat(open_date)
        
        # Make sure open_date is timezone-aware
        if open_date.tzinfo is None:
            open_date = timezone.make_aware(open_date)

        if open_date and value <= open_date:
            raise serializers.ValidationError("The closing date must be after the opening date.")
        
        return value

    def validate(self, data):
        """
        Ensure that open_date is not equal to close_date.
        """
        open_date = data.get('open_date')
        close_date = data.get('close_date')

        if open_date == close_date:
            raise serializers.ValidationError("The opening date cannot be the same as the closing date.")
        
        return data
