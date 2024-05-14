from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from employee.models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def aboutus(request):
    template="user/aboutus.html"
    return render(request,template)

def rating(request):
    template="user/complaint-rating.html"
    return render(request,template)

def statusonline(request):
    if request.session.get('user') != None:
        user = User.objects.get(email=request.session.get('user_email'))
        print(user.cuser)
        so = Status_Model.objects.filter(user=user.cuser) # filter(email=user.email)
        template="user/complaint-status-online.html"
        return render(request,template,{'form':so})
    else:
        return redirect('accounts:U_login')
    # template="user/complaint-status-online.html"
    # return render(request,template)

def statusphone(request):
    template="user/complaint-status-through-phoneorsms.html"
    return render(request,template)

def online(request):
    if request.session.get('user') != None:
        user = User.objects.get(email=request.session.get('user_email'))
        if request.method == "POST":
            cmf = Complaint_Form(request.POST,request.FILES)
            if cmf.is_valid():
                temp = cmf.save(commit=False)
                temp.username = user.cuser.profile
                temp.save()
                messages.success(request,"Your data has been submited successfully!!!")
                # Email sending to user 
                email = user.email
                print(email)
                subject = "Successfully subitmed form"
                message = "Your Complaint form is submited succesfully !!" 
                email_from = settings.EMAIL_HOST_USER
                email_to = [email, ]
                send_mail(subject, message, email_from, email_to)

                return redirect('Home:index')
            else:
                print("Insert data is not valid")
                messages.error(request,"Something went wrong!!!")
        else:
            cmf = Complaint_Form()
    else:
        return redirect('accounts:U_login')
    template = "user/online.html"
    return render(request,template,{'form':cmf,'myuser':user.cuser.profile,'user':user})
    # template="user/online.html"
    # return render(request,template)

def opinion(request):
    if request.session.get('user') != None:
        user = User.objects.get(email=request.session.get('user_email'))
        if request.method == 'POST':
            omf = Opinion_Form(request.POST)
            if omf.is_valid():
                omf_user = omf.save(commit=False)
                omf_user.user = user.cuser
                omf_user.save()
                messages.success(request,"Your data has been submited successfully!!!")
                return redirect('Home:index')
            else:
                print("Insert data is not valid")
                messages.error(request,"Something went wrong!!!")
        else: 
            omf = Opinion_Form() 
    else:
        return redirect('accounts:U_login')
    template = "user/opinion.html"
    return render(request,template,{'form':omf})
    # template="user/opinion.html"
    # return render(request,template)

def reopenemail(request):
    template="user/re-open-throughemail.html"
    return render(request,template)

def reopenonilne(request):
    if request.session.get('user') != None:
        user=User.objects.get(email=request.session.get('user_email'))
        rc = Complaint_Model.objects.filter(username=user.cuser.profile)
        template="user/re-open-throughonline.html"
        return render(request,template,{'form':rc})
    else:
        return redirect('accounts:U_login')
    # template="user/re-open-throughonline.html"
    # return render(request,template)

def reopenphone(request):
    template="user/re-open-throughphoneorsms.html"
    return render(request,template)

def email(request):
    template="user/throughemail.html"
    return render(request,template)

def phone(request):
    template="user/throughphoneorsms.html"
    return render(request,template)

def reopenview(request,id):
    if request.session.get('user') != None:
        ev = Complaint_Model.objects.get(id=id)
        template="user/reopen_view.html"
        return render(request,template,{'form':ev})
    
    


