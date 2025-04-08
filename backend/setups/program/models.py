from django.db import models

# Create your models here.
class Program(models.Model):
    program_code = models.CharField(max_length=100, unique=True)  # Code like LLM, MA, etc.
    program_name = models.TextField(max_length=100)  # Full name like Master of Laws, Master of Arts, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        return f"{self.program_code}"