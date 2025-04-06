from django.contrib import admin
from setups.application_information.models import ApplicationInformation

# Register your models here.

@admin.register(ApplicationInformation)
class ApplicationInformationAdmin(admin.ModelAdmin):
    list_display = ['admission_type', 'program', 'college', 'department', 'field_of_study', 'study_program', 'spacial_case', 'status']
    search_fields = ['admission_type__name', 'program__program_name', 'college__name', 'department__name', 'field_of_study__field_of_study', 'study_program__program_name', 'spacial_case']
    list_filter = ['status', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = ['admission_type']
    list_editable = ['status']