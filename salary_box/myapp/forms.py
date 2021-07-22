from django import forms
from .models import *


class addCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class addEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'address', 'experience')
