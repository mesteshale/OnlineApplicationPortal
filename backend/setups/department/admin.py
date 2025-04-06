from django.contrib import admin
from setups.department.models import Department
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'description']
    search_fields = ['name', 'college', 'description']
    list_filter = ['created_at', 'updated_at']
    # date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = ['name']   