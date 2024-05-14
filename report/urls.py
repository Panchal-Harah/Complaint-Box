from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('complaintreport/',complainlist.as_view(),name="cr"),
    path('cityreport/',city.as_view(),name="city"),
    path('complaint_type/',complainttype.as_view(),name="complaint_type"),
    path('feedbackreport/',feedback.as_view(),name="feedback"),
    path('statusreport/',status.as_view(),name="status"),
    # path('search/',search.as_view(),name="search")
]
