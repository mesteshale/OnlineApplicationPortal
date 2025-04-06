from rest_framework import serializers
from .models import Program

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'program_code', 'program_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        
    def validate_program_code(self, value):
        # Check if the program_code already exists in the database
        if Program.objects.filter(program_code=value).exists():
            raise serializers.ValidationError(f"The program code {value} is already in use.")
        return value