from django.core.management.base import BaseCommand
from django.db import transaction
from setups.college.models import College
from setups.department.models import Department
from setups.program.models import Program
from setups.admission_type.models import AdmissionType
from setups.study_field.models import StudyField
from setups.study_program.models import StudyProgram
from setups.application_information.models import ApplicationInformation

class Command(BaseCommand):
    help = 'Adds sample data to the ApplicationInformation model'

    def handle(self, *args, **options):
        self.stdout.write('Adding sample data to the ApplicationInformation model...')
        
        with transaction.atomic():
            # Create sample colleges if they don't exist
            college1, _ = College.objects.get_or_create(
                name='College of Computing and Informatics',
                defaults={'description': 'College of Computing and Informatics'}
            )
            college2, _ = College.objects.get_or_create(
                name='College of Business and Economics',
                defaults={'description': 'College of Business and Economics'}
            )
            college3, _ = College.objects.get_or_create(
                name='College of Medicine and Health Sciences',
                defaults={'description': 'College of Medicine and Health Sciences'}
            )
            
            # Create sample departments if they don't exist
            dept1, _ = Department.objects.get_or_create(
                name='Computer Science',
                defaults={'college': college1, 'description': 'Computer Science Department'}
            )
            dept2, _ = Department.objects.get_or_create(
                name='Information Technology',
                defaults={'college': college1, 'description': 'Information Technology Department'}
            )
            dept3, _ = Department.objects.get_or_create(
                name='Software Engineering',
                defaults={'college': college1, 'description': 'Software Engineering Department'}
            )
            dept4, _ = Department.objects.get_or_create(
                name='Accounting',
                defaults={'college': college2, 'description': 'Accounting Department'}
            )
            dept5, _ = Department.objects.get_or_create(
                name='Management',
                defaults={'college': college2, 'description': 'Management Department'}
            )
            dept6, _ = Department.objects.get_or_create(
                name='Economics',
                defaults={'college': college2, 'description': 'Economics Department'}
            )
            dept7, _ = Department.objects.get_or_create(
                name='Medicine',
                defaults={'college': college3, 'description': 'Medicine Department'}
            )
            dept8, _ = Department.objects.get_or_create(
                name='Nursing',
                defaults={'college': college3, 'description': 'Nursing Department'}
            )
            dept9, _ = Department.objects.get_or_create(
                name='Public Health',
                defaults={'college': college3, 'description': 'Public Health Department'}
            )
            
            # Create sample programs if they don't exist
            program1, _ = Program.objects.get_or_create(
                program_code='MSc',
                defaults={'program_name': 'Master of Science'}
            )
            program2, _ = Program.objects.get_or_create(
                program_code='PhD',
                defaults={'program_name': 'Doctor of Philosophy'}
            )
            
            # Create sample admission types if they don't exist
            admission_type1, _ = AdmissionType.objects.get_or_create(
                name='Regular',
                defaults={'description': 'Regular admission'}
            )
            admission_type2, _ = AdmissionType.objects.get_or_create(
                name='Extension',
                defaults={'description': 'Extension admission'}
            )
            admission_type3, _ = AdmissionType.objects.get_or_create(
                name='Distance',
                defaults={'description': 'Distance admission'}
            )
            
            # Create sample study fields if they don't exist
            field1, _ = StudyField.objects.get_or_create(
                name='Computer Science',
                defaults={'description': 'Computer Science field'}
            )
            field2, _ = StudyField.objects.get_or_create(
                name='Information Technology',
                defaults={'description': 'Information Technology field'}
            )
            field3, _ = StudyField.objects.get_or_create(
                name='Software Engineering',
                defaults={'description': 'Software Engineering field'}
            )
            field4, _ = StudyField.objects.get_or_create(
                name='Accounting and Finance',
                defaults={'description': 'Accounting and Finance field'}
            )
            field5, _ = StudyField.objects.get_or_create(
                name='Business Administration',
                defaults={'description': 'Business Administration field'}
            )
            field6, _ = StudyField.objects.get_or_create(
                name='Economics',
                defaults={'description': 'Economics field'}
            )
            field7, _ = StudyField.objects.get_or_create(
                name='Medicine',
                defaults={'description': 'Medicine field'}
            )
            field8, _ = StudyField.objects.get_or_create(
                name='Nursing',
                defaults={'description': 'Nursing field'}
            )
            field9, _ = StudyField.objects.get_or_create(
                name='Public Health',
                defaults={'description': 'Public Health field'}
            )
            
            # Create sample study programs if they don't exist
            study_program1, _ = StudyProgram.objects.get_or_create(
                name='Regular',
                defaults={'description': 'Regular study program'}
            )
            study_program2, _ = StudyProgram.objects.get_or_create(
                name='Extension',
                defaults={'description': 'Extension study program'}
            )
            study_program3, _ = StudyProgram.objects.get_or_create(
                name='Distance',
                defaults={'description': 'Distance study program'}
            )
            
            # Create sample application information entries
            # Computer Science - MSc - Regular
            ApplicationInformation.objects.get_or_create(
                college=college1,
                department=dept1,
                program=program1,
                field_of_study=field1,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Computer Science - MSc - Extension
            ApplicationInformation.objects.get_or_create(
                college=college1,
                department=dept1,
                program=program1,
                field_of_study=field1,
                study_program=study_program2,
                admission_type=admission_type2,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Information Technology - MSc - Regular
            ApplicationInformation.objects.get_or_create(
                college=college1,
                department=dept2,
                program=program1,
                field_of_study=field2,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Software Engineering - MSc - Regular
            ApplicationInformation.objects.get_or_create(
                college=college1,
                department=dept3,
                program=program1,
                field_of_study=field3,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Accounting - MSc - Regular
            ApplicationInformation.objects.get_or_create(
                college=college2,
                department=dept4,
                program=program1,
                field_of_study=field4,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Management - MSc - Regular
            ApplicationInformation.objects.get_or_create(
                college=college2,
                department=dept5,
                program=program1,
                field_of_study=field5,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Economics - MSc - Regular
            ApplicationInformation.objects.get_or_create(
                college=college2,
                department=dept6,
                program=program1,
                field_of_study=field6,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Medicine - PhD - Regular
            ApplicationInformation.objects.get_or_create(
                college=college3,
                department=dept7,
                program=program2,
                field_of_study=field7,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '3',
                    'status': True
                }
            )
            
            # Nursing - MSc - Extension
            ApplicationInformation.objects.get_or_create(
                college=college3,
                department=dept8,
                program=program1,
                field_of_study=field8,
                study_program=study_program2,
                admission_type=admission_type2,
                defaults={
                    'spacial_case': '',
                    'duration': '2',
                    'status': True
                }
            )
            
            # Public Health - PhD - Regular
            ApplicationInformation.objects.get_or_create(
                college=college3,
                department=dept9,
                program=program2,
                field_of_study=field9,
                study_program=study_program1,
                admission_type=admission_type1,
                defaults={
                    'spacial_case': '',
                    'duration': '3',
                    'status': True
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully added sample data to the ApplicationInformation model!'))
