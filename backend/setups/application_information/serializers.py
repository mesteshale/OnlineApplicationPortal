from rest_framework import serializers
from .models import ApplicationInformation

class ApplicationInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationInformation
        fields = ['id', 'admission_type', 'program', 'college', 'department', 'field_of_study', 'study_program', 'spacial_case', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']