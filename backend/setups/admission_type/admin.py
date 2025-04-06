from django.contrib import admin
from setups.admission_type.models import AdmissionType
# Register your models here.
@admin.register(AdmissionType)
class AdmissionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']
    # date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = ['name']