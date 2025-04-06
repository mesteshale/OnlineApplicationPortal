from rest_framework import serializers
from .models import StudyProgram

class StudyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgram
        fields = ['id', 'program_code', 'program_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 
        
    def validate_program_code(self, value):
        # Check if the program_code already exists in the database
        if StudyProgram.objects.filter(program_code=value).exists():
            raise serializers.ValidationError(f"The program code {value} is already in use.")
        return value