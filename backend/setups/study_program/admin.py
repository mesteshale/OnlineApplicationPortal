from django.contrib import admin
from setups.study_program.models import StudyProgram

# Register your models here.

@admin.register(StudyProgram)
class StudyProgramAdmin(admin.ModelAdmin):
    list_display = ['program_code', 'program_name']
    search_fields = ['program_code', 'program_name']
    list_filter = ['created_at', 'updated_at']
    # date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = ['program_code']