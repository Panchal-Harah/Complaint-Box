from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.                           

def index(request):
    template='user/index.html'
    return render(request,template)

