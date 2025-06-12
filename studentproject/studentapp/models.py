from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$', message='Enter a valid 10-digit phone number.')
    ])
    email = models.EmailField(validators=[EmailValidator()])
    location = models.CharField(max_length=100)
    dob = models.DateField()
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)

    def __str__(self):
        return self.name
