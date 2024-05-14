from django.urls import path
from .views import *

app_name = "Home"

urlpatterns = [
    path('',index,name='index')
]


