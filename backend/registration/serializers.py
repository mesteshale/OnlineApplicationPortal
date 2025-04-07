from rest_framework import serializers
from .models import (
    ApplicantInformation, 
    ApplicantGAT, 
    ApplicantProgramSelection, 
    ApplicantDocumentation,
    ApplicantPayment
)

class ApplicantInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantInformation
        fields = '__all__'
        read_only_fields = ['application_num', 'created_at', 'updated_at']

class ApplicantGATSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantGAT
        fields = '__all__'

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