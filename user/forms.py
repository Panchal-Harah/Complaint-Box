from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import *


class Opinion_Form(forms.ModelForm):
     class Meta:
        model = Opinion_Model
        fields = ['redio', 'text']
        widgets = {
            'redio' : forms.RadioSelect(attrs={
            }),
            'text' : forms.Textarea(attrs={
                        'class' : 'form-control',
                        'rows' : 3
            })
        }



class Complaint_Form(forms.ModelForm):
    class Meta:
        model = Complaint_Model
        fields = ['complaint_type', 'date', 'pincode', 'complaint_picture']
        widgets = {
            'complaint_type': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'city': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'date': forms.DateInput(attrs={
                'class': 'form-control  form-control-lg',
                'type': 'date'
            }),
            'pincode': forms.NumberInput(attrs={
                'class': 'form-control  form-control-lg',
                'placeholder': 'Enter Your Pincode'
            }),
            'complaint_picture': forms.FileInput(attrs={
                'class': "text-center center-block file-upload",
                'type': 'file'
            })
        }
