from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from user.models import *
from django.db.models import *


# Create your views here.

def ehome(request):
    data = Complaint_Model.objects.all()
    count1 = data.aggregate(Count('username'))
    data = Status_Model.objects.all()
    pandding = 0
    under = 0
    Completed = 0
    closed = 0
    
    for i in data:
        if i.status_type == "pandding":
            pandding += 1
        elif i.status_type == "Under Process":
            under += 1
        elif i.status_type == "Completed":
            Completed += 1
        elif i.status_type == "Closed":
            closed += 1
        else:
            pass
        
    context = {
        'pandding' : pandding,
        'under' : under,
        'Completed' : Completed,
        'closed' : closed,
        'count':count1
    }
    template="employee/emp_home.html"
    return render(request,template,context)

def empabout(request):
    template="employee/emp_aboutus.html"
    return render(request,template)

def empstatus(request,id):
    if request.session.get('employee') != None:
        data = Complaint_Model.objects.get(id=id)
        user = User.objects.get(username__iexact=data.username)
        usr = cuser.objects.get(user=user)
        if Status_Model.objects.filter(user=usr).exists() == True:
            a = Status_Model.objects.get(user=usr)
        else:
            a = None
        if request.method == "POST":
            sc = Status_Form(request.POST,request.FILES,instance=a)
            if sc.is_valid():
                temp = sc.save(commit=False)
                temp.user = usr 
                temp.save()
                messages.success(request,"Your data has been submited successfully!!!")
                return redirect('employee:ehome')
            else:
                print("Insert data is not valid")
                messages.error(request,"Something went wrong!!!")
        else:
            sc = Status_Form(instance=a)
    else:
        return redirect('accounts:E_login')
    template = "employee/emp_generate_status.html"
    return render(request,template,{'form':sc})

def empdetails(request):
    if request.session.get('employee') != None:
        user = User.objects.get(email=request.session.get('employee_email'))
        # print(user.employee.employee_profile.city)
        temp = Complaint_Model.objects.filter(username__city__iexact=user.employee.employee_profile.city)
        template="employee/employeemain.html"
        return render(request,template,{'form':temp})
    else:
        return redirect('accounts:E_login')

def empfeedback(request):
    if request.session.get('employee') != None:
        feed = Opinion_Model.objects.all()
        template="employee/E_view_feedback.html"
        return render(request,template,{'form':feed})
    else:
        return redirect('accounts:E_login')
    
def E_view(request,id):
    if request.session.get('employee') != None:
        ev = Complaint_Model.objects.get(id=id)
        print(ev.username.user.user.email)
        template="employee/E_view.html"
        return render(request,template,{'form':ev})
    else:
        return redirect('accounts:E_login')
    # template="employee/E_view.html"
    # return render(request,template)
    
# def remove_data(request,id):
#     ev = Complaint_Model.objects.get(id=id)
#     ev.delete()
#     print("data deleted successfully!!!!!")
#     return redirect('employee:empdetails')  