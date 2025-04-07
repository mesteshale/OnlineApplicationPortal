from django.db import models
from django.contrib.auth.models import User
from setups.application_information.models import ApplicationInformation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


# A utility function for generating application numbers
def generate_application_num():
    # Example of generating a unique application number (you can modify this logic based on your requirements)
    return f"APP{str(User.objects.count() + 1).zfill(4)}"

class ApplicantInformation(models.Model):
    # Linking to the User model (author) for the user who applied
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='applicant_info')

    # Basic applicant info
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)

    # Undergraduate details
    ug_university = models.CharField(max_length=255)
    ug_field_of_study = models.CharField(max_length=255)
    ug_CGPA = models.DecimalField(max_digits=4, decimal_places=2)

    # Postgraduate details (optional)
    pg_university = models.CharField(max_length=255, null=True, blank=True)
    pg_field_of_study = models.CharField(max_length=255, null=True, blank=True)
    pg_CGPA = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    # Automatically generate a unique application number
    application_num = models.CharField(max_length=5, unique=True, default=generate_application_num)

    # Registrar and Department approval information
    registrar_off_status = models.CharField(max_length=50)
    reg_approved_by = models.ForeignKey(User, related_name='registrar_approvals', null=True, blank=True, on_delete=models.SET_NULL)

    department_status = models.CharField(max_length=50)
    dep_approved_by = models.ForeignKey(User, related_name='department_approvals', null=True, blank=True, on_delete=models.SET_NULL)

    # Additional fields
    remark = models.TextField(null=True, blank=True)
    payment_status = models.CharField(max_length=50)
    telebirr_id = models.CharField(max_length=50, null=True, blank=True)

    # Timestamps for creation and updates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.application_num}"
    
#################################################################################################################

class ApplicantGAT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GAT_No = models.CharField(max_length=12, unique=True)
    GAT_Result = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.user.username} - {self.GAT_No}"
    
#################################################################################################################

class ApplicantProgramSelection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field_of_study = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.field_of_study}"
    
#################################################################################################################

class ApplicantProgramSelection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field_of_study = models.ForeignKey(ApplicationInformation, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.field_of_study.program_name}"

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    telebirr_id = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateField()
    payment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Payment"