from django.contrib import admin
from setups.registration_period.models import RegistrationPeriod
# Register your models here.
@admin.register(RegistrationPeriod)
class RegistrationPeriodAdmin(admin.ModelAdmin):
    list_display = ['name', 'open_date', 'close_date', 'is_active']
    search_fields = ['name', 'open_date', 'close_date']
    list_filter = ['is_active']
    ordering = ['open_date']
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = ['name']