from rest_framework import serializers
from .models import StudyField

class StudyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyField
        fields = ['id', 'field_of_study', 'college', 'department', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']