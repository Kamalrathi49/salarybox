from django.db.models import fields
from django.forms import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
                'username': TextInput(attrs={
                    'class': "form-control",
                    'style': 'width: 300px;',
                    'placeholder': 'Username'
                    }),
                'email': EmailInput(attrs={
                    'class': "form-control", 
                    'style': 'width: 300px;',
                    'placeholder': 'Email'
                    }),
                'password1': PasswordInput(attrs={
                    'class': "form-control",
                    'style': "width: 300px",
                    'placeholder': 'Password'
                }),
                'password2': PasswordInput(attrs={
                    'class': "form-control",
                    'style': "width: 300px",
                    'placeholder': 'Confirm Password'
                }),
                }


    def __init__(self, *args, **kwargs):
            super(signupform, self).__init__(*args, **kwargs) # Call to ModelForm constructor
            for fieldname in ['username', 'email', 'password1', 'password2']:
             self.fields[fieldname].help_text = None



   
class loginForm(forms.Form):
    username = forms.CharField(max_length=99)
    password = forms.CharField(widget=forms.PasswordInput())

    widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'placeholder': 'Username'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;',
                'placeholder': 'Password'
                }),
            
        }