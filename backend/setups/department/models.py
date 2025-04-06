from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255,verbose_name=_("Department Name"))
    college = models.ForeignKey('college.College',on_delete=models.CASCADE,verbose_name=_("College"),related_name='departments')
    description = models.TextField(max_length=255, verbose_name=_("Description"),blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")
        ordering = ['name']  # Default ordering

    def __str__(self):
        return f"{self.name} ({self.college.name})"