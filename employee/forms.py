from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import *


class Status_Form(forms.ModelForm): 
     class Meta:
        model = Status_Model
        fields = ['status_type', 'status_picture']
        widgets = {
            'status_type' : forms.Select(attrs={
                'class': 'form-control form-control-lg'
            }),
            'status_picture': forms.ClearableFileInput(attrs={
                'class': "text-center center-block file-upload",
                'type': 'file'
            })
        }