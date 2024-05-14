from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from user.models import *
from .render import Render
from employee.models import *
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request,'report/reports.html')

class complainlist(View):
    def get(self, request):
        if request.session.get('user')!= None:
            user=User.objects.get(email=request.session.get('user_email'))
            data = Complaint_Model.objects.all()
            today = timezone.now()
            params = {
                'user' :user,
                'data': data,
                'request': request,
                'today': today,
            }
        return Render.render('report/complaintreport.html', params)
    
class city(View):
    def get(self, request):
        query = request.GET['query']
        if request.session.get('user')!=None:
            user=User.objects.get(email=request.session.get('user_email'))
            data = Complaint_Model.objects.filter(username__city__icontains = query)
            today = timezone.now()
            params = {
                'user' :user,
                'data': data,
                'request': request,
                'today': today,
            }
        return Render.render('report/complaintreport.html', params)
    
class complainttype(View):
    def get(self, request):
        query = request.GET['query']
        if request.session.get('user')!=None:
            user=User.objects.get(email=request.session.get('user_email'))
            data = Complaint_Model.objects.filter(complaint_type__icontains = query)
            today = timezone.now()
            params = {
                'user' :user,
                'data': data,
                'request': request,
                'today': today,
            }
        return Render.render('report/complaint_type.html', params)
    
class feedback(View):
    def get(self, request):
        if request.session.get('user')!=None:
            user=User.objects.get(email=request.session.get('user_email'))
            data = Opinion_Model.objects.all()
            today = timezone.now()
            params = {
                'user' :user,
                'data': data,
                'request': request,
                'today': today,
            }
        return Render.render('report/feedback.html', params)

class status(View):
    def get(self, request):
        query = request.GET['query']
        if request.session.get('user')!=None:
            user=User.objects.get(email=request.session.get('user_email'))
            data = Status_Model.objects.filter(status_type__icontains=query)
            today = timezone.now()
            params = {
                'user' :user,
                'data': data,
                'request': request,
                'today': today,
            }
        return Render.render('report/status.html', params)
    
# class search(View):
#     def get(self, request):
#         query = request.GET['query']
#         if request.session.get('user')!=None:
#             user=User.objects.get(email=request.session.get('user_email'))
#             data = Complaint_Model.objects.filter(username__city__icontains=query) 
#             today = timezone.now()
#             params = {
#                 'user' :user,
#                 'data': data,
#                 'request': request,
#                 'today': today,
#             }
#         return Render.render('report/complaintreport.html',params)
    # return HttpResponse('This is search')
    