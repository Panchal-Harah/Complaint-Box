from django.urls import path
from .views import *

app_name = "employee"

urlpatterns = [
    path('',ehome,name='ehome'),
    path('empabout/',empabout,name='empabout'),
    path('empstatus/<int:id>/',empstatus,name='empstatus'),
    path('empdetails/',empdetails,name='empdetails'),
    path('empfeedback/',empfeedback,name='empfeedback'),
    path('E_view/<int:id>/',E_view,name='E_view'),
    # path('remove_data/<int:id>/',remove_data,name='remove_data')
]
