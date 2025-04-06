from django.db.models import fields
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class RegistrationPeriod(models.Model):
    name = models.CharField(max_length=100)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def is_open(self):
        # """Check if the registration period is currently open."""
        now = timezone.now()
        return self.open_date <= now <= self.close_date and self.is_active

    def clean(self):
        # """Ensure that the open_date is after the current time and the close_date is after the open_date."""
        
        now = timezone.now()

        # Check if the open_date is after the current time
        if self.open_date <= now:
            raise ValidationError("The opening date must be after the current date and time.")

        # Check if close_date is greater than open_date
        if self.open_date and self.close_date and self.open_date >= self.close_date:
            raise ValidationError("The closing date must be greater than the opening date.")

        # Ensure both open_date and close_date are set
        if not self.open_date or not self.close_date:
            raise ValidationError("Both open_date and close_date must be set.")

    def __str__(self):
        return f"{self.name} ({self.open_date} to {self.close_date})"
