from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import *


class addCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'founder', 'headquator', 'fund_raise', 'working')

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'placeholder': 'Name'
                }),
            'founder': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Founder'
                }),
            'headquator': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Headquator'
                }),
            'fund_raise': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Fund Raise'
                }),
        }


class addEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'address', 'experience')
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Last Name'
                }),
            'address': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Address'
                }),
            'experience': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Experience'
                }),
        }
