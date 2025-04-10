from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from setups.application_information.models import ApplicationInformation
from setups.sponsorship.models import Sponsorship
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import FileExtensionValidator


# A utility function for generating application numbers
def generate_application_num():
    # Generate a unique application number with a prefix and padded number
    count = User.objects.count() + 1
    # Format: A followed by a 4-digit number
    return f"A{str(count).zfill(4)}"

class ApplicantInformation(models.Model):
    # Linking to the User model (author) for the user who applied
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='applicant_info')

    # Basic applicant info - using User model's first_name and last_name
    # These fields will be used to display the user's name from the User model
    # first_name and last_name are stored in the User model
    grandfather_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    sponsorship = models.ForeignKey(Sponsorship, on_delete=models.SET_NULL,null=True,blank=True,related_name='applicants')

    # Undergraduate details
    ug_university = models.CharField(max_length=255)
    ug_field_of_study = models.CharField(max_length=255)
    ug_CGPA = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(2.0, message="CGPA must be at least 2.0"),
            MaxValueValidator(4.0, message="CGPA cannot exceed 4.0")
        ]
    )

    # Postgraduate details (optional)
    pg_university = models.CharField(max_length=255, null=True, blank=True)
    pg_field_of_study = models.CharField(max_length=255, null=True, blank=True)
    pg_CGPA = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(2.0, message="CGPA must be at least 2.0"),
            MaxValueValidator(4.0, message="CGPA cannot exceed 4.0")
        ]
    )

    # Automatically generate a unique application number
    application_num = models.CharField(max_length=10, unique=True, default=generate_application_num)

    # Registrar and Department approval information
    registrar_off_status = models.CharField(max_length=50, default='Pending')
    reg_approved_by = models.ForeignKey(User, related_name='registrar_approvals', null=True, blank=True, on_delete=models.SET_NULL)

    department_status = models.CharField(max_length=50, default='Pending')
    dep_approved_by = models.ForeignKey(User, related_name='department_approvals', null=True, blank=True, on_delete=models.SET_NULL)

    # Additional fields
    remark = models.TextField(null=True, blank=True)
    payment_status = models.BooleanField(default='False')
    telebirr_id = models.CharField(max_length=100, null=True, blank=True)

    # Timestamps for creation and updates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.application_num}"

#################################################################################################################

class ApplicantGAT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GAT_No = models.CharField(max_length=12)
    GAT_Result = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        # Ensure each user can only have one GAT record
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_user_gat')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.GAT_No}"



#################################################################################################################

class ApplicantProgramSelection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    application_info = models.ForeignKey(ApplicationInformation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Update the updated_at field on every save
        self.updated_at = timezone.now()
        if not self.id:  # If this is a new record
            self.created_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        # Ensure each user can only have one program selection record
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_user_program_selection')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.application_info}"

#################################################################################################################

# Custom validator to check file size (max 2MB)
def validate_file_size(file):
    max_size = 2 * 1024 * 1024  # 2MB in bytes
    if file.size > max_size:
        raise ValidationError("File size must be less than 2MB.")

class ApplicantDocumentation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # File fields for document uploads

    # File fields for document uploads with validation for file types
    degree = models.FileField(upload_to='uploads/degree/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg', 'jpeg', 'png']),validate_file_size])
    sponsorship = models.FileField(upload_to='uploads/sponsorship/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_file_size])
    student_copy = models.FileField(upload_to='uploads/student_copy/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg', 'jpeg', 'png']),validate_file_size])
    recommendation = models.FileField(upload_to='uploads/recommendation/', null=True,blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_file_size])
    costsharing = models.FileField(upload_to='uploads/costsharing/', null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg', 'jpeg', 'png']),validate_file_size])
    publication = models.FileField(upload_to='uploads/publication/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_file_size])
    conceptnote = models.FileField(upload_to='uploads/conceptnote/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf']),validate_file_size])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Documentation"

#################################################################################################################

class ApplicantPayment(models.Model):
    # Payment status choices
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Verified', 'Verified'),
        ('Rejected', 'Rejected'),
        ('Refunded', 'Refunded'),
    ]

    # Payment method choices
    PAYMENT_METHOD_CHOICES = [
        ('TeleBirr', 'TeleBirr'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash', 'Cash'),
    ]

    # User relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='payment')

    # Payment details
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Payment amount in ETB",
        validators=[MinValueValidator(0, message="Payment amount cannot be negative")]
    )
    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
        default='Pending',
        help_text="Current status of the payment"
    )
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        help_text="Method used for payment"
    )

    # Transaction identifiers (optional based on payment method)
    telebirr_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="TeleBirr transaction ID (required for TeleBirr payments)"
    )
    transaction_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Bank transaction ID (required for bank transfers)"
    )

    # Payment date and time
    payment_date = models.DateField(help_text="Date of payment")
    payment_time = models.TimeField(help_text="Time of payment")

    # Verification details
    verified_by = models.ForeignKey(
        User,
        related_name='verified_payments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Admin user who verified the payment"
    )
    verification_date = models.DateTimeField(null=True, blank=True, help_text="Date and time of payment verification")
    verification_note = models.TextField(null=True, blank=True, help_text="Notes about payment verification or rejection")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Applicant Payment"
        verbose_name_plural = "Applicant Payments"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.payment_amount} ETB - {self.payment_status}"

    def clean(self):
        # Validate that TeleBirr ID is provided for TeleBirr payments
        if self.payment_method == 'TeleBirr' and not self.telebirr_id:
            raise ValidationError({'telebirr_id': 'TeleBirr ID is required for TeleBirr payments'})

        # Validate that transaction ID is provided for bank transfers
        if self.payment_method == 'Bank Transfer' and not self.transaction_id:
            raise ValidationError({'transaction_id': 'Transaction ID is required for bank transfers'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)