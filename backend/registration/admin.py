from django.contrib import admin
from .models import ApplicantInformation
from .models import ApplicantGAT, ApplicantProgramSelection, ApplicantDocumentation, ApplicantPayment
# Register your models here.
admin.site.register(ApplicantInformation)
admin.site.register(ApplicantGAT)
@admin.register(ApplicantProgramSelection)
class ApplicantProgramSelectionAdmin(admin.ModelAdmin):
    exclude = ('id', 'created_at', 'updated_at')
admin.site.register(ApplicantDocumentation)
admin.site.register(ApplicantPayment)



