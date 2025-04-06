from django.contrib import admin
from setups.study_field.models import StudyField
# Register your models here.
@admin.register(StudyField)
class StudyFieldAdmin(admin.ModelAdmin):
    list_display = ['field_of_study', 'college', 'department', 'description']
    search_fields = ['field_of_study', 'college', 'department', 'description']
    list_filter = ['created_at', 'updated_at']
    # date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 20
    list_max_show_all = 100
