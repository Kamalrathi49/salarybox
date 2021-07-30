from django.db.models import fields
from django.forms import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

signup_choices =  (
    ('company', 'COMPANY'),
    ('employee', 'EMPLOYEE')
)


class signupform(UserCreationForm):
    category = forms.ChoiceField(choices=signup_choices, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'category')

    def __init__(self, *args, **kwargs):
            super(signupform, self).__init__(*args, **kwargs) # Call to ModelForm constructor
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['placeholder'] = 'Email'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
            self.fields['category'].widget.attrs['class'] = 'form-control'
            self.fields['category'].widget.attrs['placeholder'] = 'SignUp as'
            for fieldname in ['username', 'email', 'password1', 'password2']:
             self.fields[fieldname].help_text = None
