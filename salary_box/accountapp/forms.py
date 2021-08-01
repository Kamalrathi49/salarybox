from django.db.models import fields
from django.forms import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class signupform(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }),
        }

    def __init__(self, *args, **kwargs):
        # Call to ModelForm constructor
        super(signupform, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class loginForm(forms.Form):
    username = forms.CharField(max_length=99, widget=forms.TextInput(attrs={
        'class': 'form-control',  'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}))
