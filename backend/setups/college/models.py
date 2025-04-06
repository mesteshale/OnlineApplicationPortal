from django.db import models

# Create your models here. 
class College(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"