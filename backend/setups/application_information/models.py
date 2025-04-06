from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ApplicationInformation(models.Model):
    admission_type = models.ForeignKey('admission_type.AdmissionType', on_delete=models.CASCADE, verbose_name=_('Admission Type'))
    program = models.ForeignKey('program.Program', on_delete=models.CASCADE, verbose_name=_('Program'))
    college = models.ForeignKey('college.College', on_delete=models.CASCADE, verbose_name=_('College'))
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE, verbose_name=_('Department'))
    field_of_study = models.ForeignKey('study_field.StudyField', on_delete=models.CASCADE, verbose_name=_('Field of Study'))
    study_program = models.ForeignKey('study_program.StudyProgram', on_delete=models.CASCADE, verbose_name=_('Study Program'))
    spacial_case = models.CharField(max_length=255, verbose_name=_('Special Case'), blank=True)
    status = models.BooleanField(default=True, verbose_name=_('Active Status'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Application Information')
        verbose_name_plural = _('Application Information')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.admission_type.name} - {self.program.program_name} - {self.college.name} - {self.department.name} - {self.field_of_study.field_of_study} - {self.study_program.program_name}"