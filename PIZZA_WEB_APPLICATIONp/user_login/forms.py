from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class Add_user(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = {
        "username": forms.TextInput(attrs={'class': 'form-control'}), 
        "email" : forms.TextInput(attrs={'class': 'form-control'}),
        'phone_number' :  forms.TextInput(attrs={'class': 'form-control'}),
        "password1": forms.TextInput(attrs={'class': 'form-control'}),
        "password2":forms.TextInput(attrs={'class': 'form-control'}),

        }

      
