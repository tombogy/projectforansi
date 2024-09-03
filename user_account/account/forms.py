

from django import forms
from .models import Driver

class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'mobile', 'license', 'email', 'did', 'password', 'photo']
        widgets = {
            'password': forms.PasswordInput(),
        }
