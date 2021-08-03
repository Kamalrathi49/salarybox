from django.db.models import fields
from django.forms import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class signupform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
     'class': 'form-control', 'placeholder': 'Email Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}),label=(u'Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'}),label=(u'Confirm Password'))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        # Call to ModelForm constructor
        super(signupform, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean(self):
 
        # data from the form is fetched using super function
        super(signupform, self).clean()
         
        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
 
        # conditions to be met for the username length
        if len(username) > 12 and username.isalnum():
            self._errors['username'] = self.error_class([
                'Username shound be less then 12 characters'])
        if len(email) <10:
            self._errors['email'] = self.error_class([
                "email should contain '@' and '.com'"])
 
        # return any errors if found
        return self.cleaned_data


class loginForm(forms.Form):
    username = forms.CharField(max_length=99, widget=forms.TextInput(attrs={
        'class': 'form-control',  'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}))
