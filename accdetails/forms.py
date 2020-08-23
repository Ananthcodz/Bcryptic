from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import AccountDetails

class SignUP(UserCreationForm):
    FirstName = forms.CharField(max_length=100)           
    LastName = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    Address = forms.CharField(max_length=200)

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1','password2','Address')    