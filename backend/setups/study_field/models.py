from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class StudyField(models.Model):

    field_of_study = models.CharField(max_length=255,verbose_name=_("Field of Study"))
    college = models.ForeignKey('college.College',on_delete=models.CASCADE,verbose_name=_("College"), related_name='field_of_studies')
    department = models.ForeignKey('department.Department',on_delete=models.CASCADE, verbose_name=_("Department"),related_name='field_of_studies')
    description = models.TextField(verbose_name=_("Description"), blank=True)
    status = models.BooleanField(default=True,verbose_name=_("Active Status"))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Field of Study")
        verbose_name_plural = _("Fields of Study")
        ordering = ['field_of_study']  # Default ordering

    def __str__(self):
        return f"{self.field_of_study} ({self.department.name})"
    
     

