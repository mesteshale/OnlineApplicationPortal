from rest_framework import serializers
from .models import ApplicationInformation
from setups.college.models import College
from setups.department.models import Department
from setups.program.models import Program
from setups.admission_type.models import AdmissionType
from setups.study_field.models import StudyField
from setups.study_program.models import StudyProgram

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'program_code', 'program_name']

class AdmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionType
        fields = ['id', 'name']

class StudyFieldSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='field_of_study', read_only=True)

    class Meta:
        model = StudyField
        fields = ['id', 'name']

class StudyProgramSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='program_name', read_only=True)

    class Meta:
        model = StudyProgram
        fields = ['id', 'name']

class ApplicationInformationSerializer(serializers.ModelSerializer):
    college = CollegeSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)
    admission_type = AdmissionTypeSerializer(read_only=True)
    field_of_study = StudyFieldSerializer(read_only=True)
    study_program = StudyProgramSerializer(read_only=True)

    class Meta:
        model = ApplicationInformation
        fields = ['id', 'admission_type', 'program', 'college', 'department', 'field_of_study', 'study_program', 'spacial_case', 'duration', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']