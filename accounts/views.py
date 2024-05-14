from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password 
import random
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# employee

def E_sign_up(request):
    if request.session.get('employee') != None:
        return redirect('accounts:E_profile')
    if request.method == "POST":
        ucf = E_sign_up_form(request.POST)
        if ucf.is_valid():
            if User.objects.filter(email__iexact=ucf.cleaned_data['email']):
                messages.error(request,"Email id is already registered")
            else:
                print('---------------------------------')
                if (ucf.cleaned_data['email'] == ""):
                    messages.error(request,"Email id should not be empty")
                    return redirect('accounts:empregistration')
                print('---------------------------------')
                ucf.save()
                reg = employee(user=(User.objects.get(username=ucf.cleaned_data['username'])))
                reg.save()
                user_update = User.objects.get(username=ucf.cleaned_data['username'])
                user_update.is_active = False
                user_update.save()
                messages.success(request,'Registered')
                request.session['employee_email'] = ucf.cleaned_data['email']
                request.session['employee_username'] = ucf.cleaned_data['username']
                #sending verfication mail
                subject = 'Verification Mail'
                message = f'Hello {user_update.username},' + "\nEmail : " + user_update.email + \
                    "\nPlease verify your email id.. http://127.0.0.1:8000/account/E_verify_email_fun/"
                email_from = settings.EMAIL_HOST_USER
                email_to = [user_update.email, ]
                send_mail(subject, message, email_from, email_to)
                return redirect('accounts:E_verification_mail_sent_fun')
    else:
        ucf = E_sign_up_form()
    template = "employee/emp_registration.html"
    return render(request,template,{'form':ucf})

def E_verification_mail_sent_fun(request):
    template = "employee/E_verification_sent.html"
    return render(request, template)

def E_verify_email_fun(request):
    if request.session.get('employee') != None:
        request.session.delete()
        return redirect('accounts:E_verify_email_fun')
    if request.method == "POST":
        form = E_verification_form(request.POST)
        if form.is_valid():
            email_data = form.cleaned_data['email']
            if (email_data == ""):
                messages.error(request,'Please enter valid email id')
                return redirect('accounts:E_verify_email_fun')
            if not User.objects.filter(email__iexact=email_data):
                messages.error(request,'Email and user not found, please signup!')
                return redirect('accounts:empregistration')
            usr = User.objects.get(email__iexact=email_data)
            if (usr.is_active == True) and (usr.is_staff == True):
                messages.error(request,f'{usr.email} is already activated')
                messages.error(request,'Please Login')
                return redirect('accounts:E_login')
            else:
                usr.is_active = True
                usr.is_staff = True
                usr.save()
                employee = {
                    'employee_name': usr.username, 
                    'employee_email': usr.email
                }
                request.session['employee'] = employee
                
                if (usr.is_staff == True):
                    request.session.get('employee')
                    return redirect('accounts:E_profile')
    else:
        form = E_verification_form()
    return render(request, 'employee/E_confirm_email.html',{'form':form})


# def E_log_in(request):
#     if request.session.get('employee') != None and User.is_staff == True:
#         return redirect('accounts:E_profile')
#     if request.method == "POST":
#         auf = E_log_in_form(request=request, data=request.POST)
#         if auf.is_valid():
#             user = authenticate(
#                 username = auf.cleaned_data['username'],
#                 password = auf.cleaned_data['password'],
#             )
#             if user is not None:
#                 user_data = User.objects.get(username=user)
#                 if user_data.is_active == True and user_data.is_staff == True:
#                     employee = {
#                         'employee_name' : user_data.username,
#                         'employee_email' : user_data.email
#                     }
#                     request.session['employee']  = employee
#                     request.session['employee_email'] = user_data.email
#                     return redirect('accounts:E_profile')
#                 else:
#                     messages.error(request,"User is not authenticated yet!\nPlease verify your email")
#                     return redirect('accounts:E_verify_email_fun')                    
#             else:
#                 messages.error(request,"User not found")
#                 return redirect('accounts:empregistration')
#     else:
#         auf = E_log_in_form()
#     template = "employee/E_login.html"
#     return render(request,template,{'form':auf})

def E_log_in(request):
    if request.session.get('employee') != None:
        return redirect('accounts:E_profile')
    if request.method == "POST":
        auf = E_log_in_form(request=request, data=request.POST)
        if auf.is_valid():
            user = authenticate(
                username = auf.cleaned_data['username'],
                password = auf.cleaned_data['password'],
            )
            if user is not None:
                user_data = User.objects.get(username=user)
                if user_data.is_active == True and user_data.is_staff == True:
                    user = {
                        'employee_name' : user_data.username,
                        'employee_email' : user_data.email
                    }
                    request.session['employee']  = user
                    request.session['employee_email'] = user_data.email
                    return redirect('accounts:E_profile')
                else:
                    messages.error(request,"User is not authenticated yet!\nPlease verify your email")
                    return redirect('accounts:E_verify_email_fun')                    
            else:
                messages.error(request,"User not found")
                return redirect('accounts:empregistration')
    else:
        auf = E_log_in_form()
    template = "employee/E_login.html"
    return render(request,template,{'form':auf})



def E_log_out(request):
    if (request.session.get('employee') != None):
        logout(request)
        return redirect('accounts:E_login')
    else:
        return redirect('accounts:E_login')

def E_set_password(request):
    if request.session.get('employee') == None:
        return redirect('accounts:E_login')
    user_data = request.session.get('employee')
    if request.method == "POST":
        old = request.POST.get('old_password')
        pass1 = request.POST.get('new_password1')
        pass2 = request.POST.get('new_password2')
        user = User.objects.get(email__iexact = request.session.get('employee_email'))
        if pass1 == pass2:
            if check_password(old, user.password):
                user.set_password(pass1)
                user.save()
                messages.success(request,"Password has been updated successfully!")
                return redirect("accounts:E_profile")
            else:
                messages.error(request,"old password is wrong")
                return redirect("accounts:E_set_password")
        else:
            messages.error(request,"New and Confirm password not same")
            return redirect("accounts:E_set_password")
    template = "employee/E_set_password.html"
    return render(request,template,{'name':user_data})

def E_forgot_password(request):
    if request.method == 'POST':
        f_p_form = E_forgot_password_form(request.POST)
        if f_p_form.is_valid():
            email = request.POST.get('email')
            is_email = User.objects.filter(email__iexact=email).exists()
            if is_email:
                OTP = random.randint(111111, 999999)
                subject = "Password Reset OTP"
                message = "Your OTP is, " + \
                    str(OTP) + "\nPlease Follow This Link to verify OTP, --> http://127.0.0.1:8000/account/E_otp_verify"
                email_from = settings.EMAIL_HOST_USER
                email_to = [email, ]
                send_mail(subject, message, email_from, email_to)

                # OTP and email set In Session
                request.session["reset_password_OTP"] = OTP
                request.session["reset_password_EMAIL"] = email
                request.session.set_expiry(900)
                return redirect('accounts:E_otp_verify')
            else:
               messages.error(request,"Email not found, please signup!") 
               return redirect("accounts:empregistration")
    else:
        f_p_form = E_forgot_password_form()
    template = 'employee/E_forgot_password.html'
    return render(request, template, {'form': f_p_form})

def E_otp_verify(request):
    if request.method == 'POST':
        omf = E_otp_match_form(request.POST)
        otp = request.POST.get('otp')
        session_otp = request.session.get('reset_password_OTP')
        if str(otp) == str(session_otp):
            return redirect('accounts:E_reset_password')
        else:
            messages.error(request,"Please enter valid OTP")
            return redirect('accounts:E_otp_verify')
    else:
        omf = E_otp_match_form()
    template = 'employee/E_otp_verification.html'
    return render(request, template, {'form':omf})

def E_reset_password(request):
    if request.method == 'POST':
        password = request.POST['password1']
        c_password = request.POST['password2']

        if password == c_password:
            email_var = request.session.get('reset_password_EMAIL')
            usr = User.objects.get(email=email_var)
            usr.set_password(password)
            usr.save()
            request.session.delete()
            return redirect('accounts:E_login')
    template = 'employee/E_reset_password.html'
    return render(request, template)

def E_profile(request):
    if request.session.get('employee') != None:
        uer = request.session.get('employee')
        if not User.objects.filter(username__iexact=uer['employee_name']).exists():
            messages.error(request,"User not found")
            request.session.delete()
            return redirect('accounts:E_login')
        user = User.objects.get(username=uer['employee_name'])
        if request.method == "POST":
            user_form = E_UserForm(request.POST or None, instance=user)
            profile_form = E_ProfileForm(
                request.POST or None, request.FILES or None, instance=user.employee.employee_profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Form submitted successfully')
                return redirect('accounts:E_profile')
            else:
                messages.error(request, 'Please correct the error below')
        else:
            user_form = E_UserForm(instance=user)
            profile_form = E_ProfileForm(instance=user.employee.employee_profile)
        profile_user = Employee_Profile.objects.get(user=user.employee.employee_profile)
        if profile_user.profile_pic is None:
            image = None
        else:
            image = profile_user
        template = 'employee/E_profile.html'
        return render(request, template, {'user_form': user_form, 'profile_form': profile_form,'image':image})
    else:
        return redirect('accounts:E_login')  



# user


def U_sign_up(request):
    if request.session.get('user') != None:
        return redirect('accounts:U_profile')
    if request.method == "POST":
        ucf = U_sign_up_form(request.POST)
        if ucf.is_valid():
            if User.objects.filter(email__iexact=ucf.cleaned_data['email']):
                messages.error(request,"Email id is already registered")
            else:
                print('---------------------------------')
                if (ucf.cleaned_data['email'] == ""):
                    messages.error(request,"Email id should not be empty")
                    return redirect('accounts:uregistration')
                print('---------------------------------')
                ucf.save()
                reg = cuser(user=(User.objects.get(username=ucf.cleaned_data['username'])))
                reg.save()
                user_update = User.objects.get(username=ucf.cleaned_data['username'])
                user_update.is_active = False
                user_update.save()
                messages.success(request,'Registered')
                request.session['user_email'] = ucf.cleaned_data['email']
                request.session['user_username'] = ucf.cleaned_data['username']
                #sending verfication mail
                subject = 'Verification Mail'
                message = f'Hello {user_update.username},' + "\nEmail : " + user_update.email + \
                    "\nPlease verify your email id.. http://127.0.0.1:8000/account/U_verify_email_fun/"
                email_from = settings.EMAIL_HOST_USER
                email_to = [user_update.email, ]
                send_mail(subject, message, email_from, email_to)
                return redirect('accounts:U_verification_mail_sent_fun')
    else:
        ucf = U_sign_up_form()
    template = "user/user_registration.html"
    return render(request,template,{'form':ucf})

def U_verification_mail_sent_fun(request):
    template = "user/U_verification_sent.html"
    return render(request, template)

def U_verify_email_fun(request):
    if request.session.get('user') != None:
        request.session.delete()
        return redirect('accounts:U_verify_email_fun')
    if request.method == "POST":
        form = U_verification_form(request.POST)
        if form.is_valid():
            email_data = form.cleaned_data['email']
            if (email_data == ""):
                messages.error(request,'Please enter valid email id')
                return redirect('accounts:U_verify_email_fun')
            if not User.objects.filter(email__iexact=email_data):
                messages.error(request,'Email and user not found, please signup!')
                return redirect('accounts:uregistration')
            usr = User.objects.get(email__iexact=email_data)
            if (usr.is_active == True) and (usr.is_staff == False):
                messages.error(request,f'{usr.email} is already activated')
                messages.error(request,'Please Login')
                return redirect('accounts:U_login')
            else:
                usr.is_active = True
                usr.save()
                user = {
                    'user_name': usr.username, 
                    'user_email': usr.email
                }
                request.session['user'] = user
                
                if (usr.is_staff == False):
                    request.session.get('user')
                    return redirect('accounts:U_profile')
    else:
        form = U_verification_form()
    return render(request, 'user/U_confirm_email.html',{'form':form})


def U_log_in(request):
    if request.session.get('user') != None:
        return redirect('accounts:U_profile')
    if request.method == "POST":
        auf = U_log_in_form(request=request, data=request.POST)
        if auf.is_valid():
            user = authenticate(
                username = auf.cleaned_data['username'],
                password = auf.cleaned_data['password'],
            )
            if user is not None:
                user_data = User.objects.get(username=user)
                if user_data.is_active == True and user_data.is_staff == False:
                    user = {
                        'user_name' : user_data.username,
                        'user_email' : user_data.email
                    }
                    request.session['user']  = user
                    request.session['user_email'] = user_data.email
                    return redirect('accounts:U_profile')
                else:
                    messages.error(request,"User is not authenticated yet!\nPlease verify your email")
                    return redirect('accounts:U_verify_email_fun')                    
            else:
                messages.error(request,"User not found")
                return redirect('accounts:uregistration')
    else:
        auf = U_log_in_form()
    template = "user/U_login.html"
    return render(request,template,{'form':auf})

def U_log_out(request):
    if (request.session.get('user') != None):
        logout(request)
        return redirect('accounts:U_login')
    else:
        return redirect('accounts:U_login')

def U_set_password(request):
    if request.session.get('user') == None:
        return redirect('accounts:U_login')
    user_data = request.session.get('user')
    if request.method == "POST":
        old = request.POST.get('old_password')
        pass1 = request.POST.get('new_password1')
        pass2 = request.POST.get('new_password2')
        user = User.objects.get(email__iexact = request.session.get('user_email'))
        if pass1 == pass2:
            if check_password(old, user.password):
                user.set_password(pass1)
                user.save()
                messages.success(request,"Password has been updated successfully!")
                return redirect("accounts:U_profile")
            else:
                messages.error(request,"old password is wrong")
                return redirect("accounts:U_set_password")
        else:
            messages.error(request,"New and Confirm password not same")
            return redirect("accounts:U_set_password")
    template = "user/U_set_password.html"
    return render(request,template,{'name':user_data})

def U_forgot_password(request):
    if request.method == 'POST':
        f_p_form = U_forgot_password_form(request.POST)
        if f_p_form.is_valid():
            email = request.POST.get('email')
            is_email = User.objects.filter(email__iexact=email).exists()
            if is_email:
                OTP = random.randint(111111, 999999)
                subject = "Password Reset OTP"
                message = "Your OTP is, " + \
                    str(OTP) + "\nPlease Follow This Link to verify OTP, --> http://127.0.0.1:8000/account/U_otp_verify"
                email_from = settings.EMAIL_HOST_USER
                email_to = [email, ]
                send_mail(subject, message, email_from, email_to)

                # OTP and email set In Session
                request.session["reset_password_OTP"] = OTP
                request.session["reset_password_EMAIL"] = email
                request.session.set_expiry(900)
                return redirect('accounts:U_otp_verify')
            else:
               messages.error(request,"Email not found, please signup!") 
               return redirect("accounts:uregistration")
    else:
        f_p_form = U_forgot_password_form()
    template = 'user/U_forgot_password.html'
    return render(request, template, {'form': f_p_form})

def U_otp_verify(request):
    if request.method == 'POST':
        omf = U_otp_match_form(request.POST)
        otp = request.POST.get('otp')
        session_otp = request.session.get('reset_password_OTP')
        if str(otp) == str(session_otp):
            return redirect('accounts:U_reset_password')
        else:
            messages.error(request,"Please enter valid OTP")
            return redirect('accounts:U_otp_verify')
    else:
        omf = U_otp_match_form()
    template = 'user/U_otp_verification.html'
    return render(request, template, {'form':omf})

def U_reset_password(request):
    if request.method == 'POST':
        password = request.POST['password1']
        c_password = request.POST['password2']

        if password == c_password:
            email_var = request.session.get('reset_password_EMAIL')
            usr = User.objects.get(email=email_var)
            usr.set_password(password)
            usr.save()
            request.session.delete()
            return redirect('accounts:U_login')
    template = 'user/U_reset_password.html'
    return render(request, template)

def U_profile(request):
    if request.session.get('user') != None:
        uer = request.session.get('user')
        if not User.objects.filter(username__iexact=uer['user_name']).exists():
            messages.error(request,"User not found")
            request.session.delete()
            return redirect('accounts:U_login')
        user = User.objects.get(username=uer['user_name'])
        if request.method == "POST":
            user_form = U_UserForm(request.POST or None, instance=user)
            profile_form = U_ProfileForm(
                request.POST or None, request.FILES or None, instance=user.cuser.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Form submitted successfully')
                return redirect('accounts:U_profile')
            else:
                messages.error(request, 'Please correct the error below')
        else:
            user_form = U_UserForm(instance=user)
            profile_form = U_ProfileForm(instance=user.cuser.profile)
        profile_user = Profile.objects.get(user=user.cuser.profile)
        if profile_user.profile_pic is None:
            image = None
        else:
            image = profile_user
        template = 'user/U_profile.html'
        return render(request, template, {'user_form': user_form, 'profile_form': profile_form,'image':image})
    else:
        return redirect('accounts:U_login')