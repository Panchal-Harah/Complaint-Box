from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import *

# employee


class E_sign_up_form(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':"form-control",
                'placeholder':'Enter Password'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Password Again'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
                        'class':"form-control",
                       'placeholder':'Enter Your Email'
                    }))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Your Username'
                
            }),
            'first_name' : forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Your First Name'

            }),
            'last_name' : forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Your Last Name'
            }),
        }

class E_log_in_form(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={
                        'class':"form-control",
                        'placeholder':'Enter Your Username'
                        }))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={
                        'class':"form-control",
                        'placeholder':'Enter Password'
                        }))
    class Meta:
        model = User
        fields = ['username','password']

class E_verification_form(UserCreationForm):
    password1 = None
    password2 = None
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
                        'class':"form-control",
                       'placeholder':'Enter Your Email'
                    }))    
    class Meta:
        model = User
        fields = ['email']

class E_forgot_password_form(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    class Meta:
        model = User
        fields = ['email']

class E_otp_match_form(forms.Form):
    otp = forms.CharField(required=True, error_messages={'required':'Please enter OTP'} ,max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your OTP'}))


class E_UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, disabled=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    email = forms.EmailField(max_length=50, disabled=True, widget=forms.EmailInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    
    class Meta:
        model = Employee_Profile
        fields = ['username','first_name','last_name', 'email']



class E_ProfileForm(forms.ModelForm):
	class Meta:
		model = Employee_Profile
		fields = ['area','address','tel','gender','city','age','profile_pic']
		widgets = {
        'area' : forms.TextInput(attrs={
                                'class' : 'form-control form-control-lg',
                                'placeholder' : 'Enter Your Area'
                                }),
		'tel' : forms.NumberInput(attrs={
                                'class':'form-control form-control-lg',
                                'placeholder' : 'Enter Your Phonenumber'
                                }),
		'age' : forms.NumberInput(attrs={
                                'class':'form-control form-control-lg',
                                'placeholder' : 'Enter Your Age'
                                }),
		'address' : forms.Textarea(attrs={
                                'class':'form-control form-control-lg',
                                'rows': 4,
                                'fs': '4'
                                }),
		'gender' : forms.Select(attrs={
                                'class':'form-control form-control-lg'
                                }),
        'city' : forms.Select(attrs={
                                'class' : 'form-control form-control-lg'
                                }),
        'profile_pic' : forms.FileInput(attrs={
                                'class':"text-center center-block file-upload"
                                })
        }
  
  
  
# user
  
class U_sign_up_form(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':"form-control",
                'placeholder':'Enter Password'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Password Again'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
                        'class':"form-control",
                       'placeholder':'Enter Your Email'
                    }))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Your Username'
                
            }),
            'first_name' : forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Your First Name'

            }),
            'last_name' : forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Enter Your Last Name'
            }),
        }

class U_log_in_form(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':"form-control" , 'placeholder':'Enter Password'}))
    class Meta:
        model = User
        fields = ['username','password']

class U_verification_form(UserCreationForm):
    password1 = None
    password2 = None
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
                        'class':"form-control",
                       'placeholder':'Enter Your Email'
                    }))    
    class Meta:
        model = User
        fields = ['email']

class U_forgot_password_form(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}))
    class Meta:
        model = User
        fields = ['email']

class U_otp_match_form(forms.Form):
    otp = forms.CharField(required=True, error_messages={'required':'Please enter OTP'} ,max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your OTP'}))


class U_UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, disabled=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    email = forms.EmailField(max_length=50, disabled=True, widget=forms.EmailInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']



class U_ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['area','address','tel','gender','age','profile_pic','city']
		widgets = {
        'area' : forms.TextInput(attrs={
                                'class' : 'form-control form-control-lg',
                                'placeholder' : 'Enter Your Area'
                                }),
		'tel' : forms.NumberInput(attrs={
                                'class':'form-control form-control-lg',
                                'placeholder' : 'Enter Your Phonenumber'
                                }),
		'age' : forms.NumberInput(attrs={
                                'class':'form-control form-control-lg',
                                'placeholder' : 'Enter Your Age'
                                }),
		'address' : forms.Textarea(attrs={
                                'class':'form-control form-control-lg',
                                'fs' : '4',
                                'rows': 4
                                }),
		'gender' : forms.Select(attrs={
                                'class':'form-control form-control-lg'
                                }), 
        'city' : forms.Select(attrs={
                                'class' : 'form-control form-control-lg'
                                }),
        'profile_pic' : forms.FileInput(attrs={
                                'class':"text-center center-block file-upload"
                                })
        }