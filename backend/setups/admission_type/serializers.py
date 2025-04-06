from rest_framework import serializers
from .models import AdmissionType

class AdmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionType
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']