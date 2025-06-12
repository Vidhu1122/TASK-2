from django import forms
from .models import Student
from datetime import date
import re

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z ]+$', name):
            raise forms.ValidationError("Name should contain only letters and spaces.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d{10}$', phone):
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not re.match(r'^[A-Za-z ]+$', location):
            raise forms.ValidationError("Location should contain only letters and spaces.")
        return location

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob >= date.today():
            raise forms.ValidationError("Date of birth must be in the past.")
        return dob

    def clean_college(self):
        college = self.cleaned_data.get('college')
        if not re.match(r'^[A-Za-z ]+$', college):
            raise forms.ValidationError("College name should contain only letters and spaces.")
        return college

    def clean_degree(self):
        degree = self.cleaned_data.get('degree')
        if not re.match(r'^[A-Za-z ]+$', degree):
            raise forms.ValidationError("Degree should contain only letters and spaces.")
        return degree
