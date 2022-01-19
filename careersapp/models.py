from django.db import models
from django.core.validators import RegexValidator

# class Jobs(models.Model):
#     job_title = models.CharField(max_length= 50 )
#     job_description = models.CharField(max_length = 200)

class Careers(models.Model):
    # job = models.ForeignKey(Jobs, on_delete = models.CASCADE ,related_name = 'jobs')
    full_name = models.CharField(max_length=30,default = "Your Name")
    email = models.EmailField()
    phone_regex = RegexValidator( regex = r'^\+?1?\d{9,15}$' , message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed, with country code as +91.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True ,default=" +999999999" ) # validators should be a list
    applicant_description = models.CharField(max_length=500 , default= "Enter your Description")
    # resume = models.FileField()

