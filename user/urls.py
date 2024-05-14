from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('aboutus/',aboutus,name='aboutus'),
    path('rating/',rating,name='rating'),
    path('statusonline/',statusonline,name='statusonline'),
    path('statusphone/',statusphone,name='statusphone'),
    path('online/',online,name='online'),
    path('opinion/',opinion,name='opinion'),
    path('reopenemail/',reopenemail,name='reopenemail'),
    path('reopenonilne/',reopenonilne,name='reopenonilne'),
    path('reopenphone/',reopenphone,name='reopenphone'),
    path('email/',email,name='email'),
    path('phone/',phone,name='phone'),
    path('reopen_view/<int:id>/',reopenview,name='reopen_view')
    
]
