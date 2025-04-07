from django.contrib import admin
from .models import ApplicantInformation
from .models import ApplicantGAT, ApplicantProgramSelection, ApplicantDocumentation, ApplicantPayment
# Register your models here.
admin.site.register(ApplicantInformation)
admin.site.register(ApplicantGAT)
admin.site.register(ApplicantProgramSelection)
admin.site.register(ApplicantDocumentation)
admin.site.register(ApplicantPayment)



