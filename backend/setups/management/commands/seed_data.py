from django.core.management.base import BaseCommand
from django.utils import timezone
from setups.college.models import College
from setups.department.models import Department
from setups.program.models import Program
from setups.study_field.models import StudyField
from setups.study_program.models import StudyProgram
from setups.admission_type.models import AdmissionType
from setups.registration_period.models import RegistrationPeriod
from setups.application_information.models import ApplicationInformation

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Seed Colleges
        colleges_data = [
            {
                'name': 'College of Natural and Computational Sciences',
                'description': 'CNCS offers various programs in sciences and mathematics'
            },
            {
                'name': 'College of Social Sciences and Humanities',
                'description': 'CSSH focuses on social sciences and humanities disciplines'
            },
            {
                'name': 'College of Business and Economics',
                'description': 'CBE provides education in business and economic fields'
            }
        ]

        for college in colleges_data:
            College.objects.get_or_create(
                name=college['name'],
                defaults={'description': college['description']}
            )

        # Seed Programs
        programs_data = [
            {
                'program_code': 'MA',
                'program_name': 'Master of Arts'
            },
            {
                'program_code': 'MSC',
                'program_name': 'Master of Science'
            },
            {
                'program_code': 'PHD',
                'program_name': 'Doctor of Philosophy'
            }
        ]

        for program in programs_data:
            Program.objects.get_or_create(
                program_code=program['program_code'],
                defaults={'program_name': program['program_name']}
            )

        # Seed Departments
        departments_data = [
            {
                'name': 'Computer Science',
                'description': 'Department of Computer Science',
                'college': 'College of Natural and Computational Sciences'
            },
            {
                'name': 'Economics',
                'description': 'Department of Economics',
                'college': 'College of Business and Economics'
            },
            {
                'name': 'History',
                'description': 'Department of History',
                'college': 'College of Social Sciences and Humanities'
            }
        ]

        for dept in departments_data:
            college = College.objects.get(name=dept['college'])
            Department.objects.get_or_create(
                name=dept['name'],
                defaults={
                    'description': dept['description'],
                    'college': college
                }
            )

        # Seed Study Fields
        study_fields_data = [
            {
                'name': 'Software Engineering',
                'description': 'Focus on software development and engineering principles',
                'department': 'Computer Science'
            },
            {
                'name': 'Development Economics',
                'description': 'Study of economic development in developing countries',
                'department': 'Economics'
            },
            {
                'name': 'Ancient History',
                'description': 'Study of ancient civilizations and their development',
                'department': 'History'
            }
        ]

        for field in study_fields_data:
            department = Department.objects.get(name=field['department'])
            StudyField.objects.get_or_create(
                name=field['name'],
                defaults={
                    'description': field['description'],
                    'department': department
                }
            )

        # Seed Study Programs
        study_programs_data = [
            {
                'program_code': 'MSC-SE',
                'program_name': 'MSc in Software Engineering'
            },
            {
                'program_code': 'MA-DE',
                'program_name': 'MA in Development Economics'
            },
            {
                'program_code': 'PHD-AH',
                'program_name': 'PhD in Ancient History'
            }
        ]

        for study_program in study_programs_data:
            StudyProgram.objects.get_or_create(
                program_code=study_program['program_code'],
                defaults={'program_name': study_program['program_name']}
            )

        # Seed Admission Types
        admission_types_data = [
            {
                'name': 'Regular',
                'description': 'Regular admission for full-time students'
            },
            {
                'name': 'Extension',
                'description': 'Extension program for working professionals'
            },
            {
                'name': 'Summer',
                'description': 'Summer program for intensive study'
            }
        ]

        for admission_type in admission_types_data:
            AdmissionType.objects.get_or_create(
                name=admission_type['name'],
                defaults={'description': admission_type['description']}
            )

        # Seed Registration Periods
        registration_periods_data = [
            {
                'academic_year': '2024/25',
                'semester': 1,
                'start_date': timezone.now(),
                'end_date': timezone.now() + timezone.timedelta(days=30),
                'status': True
            },
            {
                'academic_year': '2024/25',
                'semester': 2,
                'start_date': timezone.now() + timezone.timedelta(days=180),
                'end_date': timezone.now() + timezone.timedelta(days=210),
                'status': False
            }
        ]

        for period in registration_periods_data:
            RegistrationPeriod.objects.get_or_create(
                academic_year=period['academic_year'],
                semester=period['semester'],
                defaults={
                    'start_date': period['start_date'],
                    'end_date': period['end_date'],
                    'status': period['status']
                }
            )

        # Seed Application Information
        for admission_type in AdmissionType.objects.all():
            for program in Program.objects.all():
                for college in College.objects.all():
                    for department in Department.objects.filter(college=college):
                        for study_field in StudyField.objects.filter(department=department):
                            for study_program in StudyProgram.objects.all():
                                ApplicationInformation.objects.get_or_create(
                                    admission_type=admission_type,
                                    program=program,
                                    college=college,
                                    department=department,
                                    field_of_study=study_field,
                                    study_program=study_program,
                                    defaults={
                                        'spacial_case': '',
                                        'status': True
                                    }
                                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))