from django.db import models
from django_resized import ResizedImageField
from accounts.models import *


# Create your models here.
G_STATUS_CHOICES = (
    ('pandding','pandding'),
    ('Under Process', 'Under Process'),
    ('Completed', 'Completed'),
    # ('Rejected', 'Rejected'),
    ('Closed', 'Closed')
)

    
class Status_Model(models.Model):
    user = models.ForeignKey(cuser,on_delete=models.CASCADE,null=True,blank=True)
    status_type = models.CharField(
         max_length=250, choices=G_STATUS_CHOICES, default='pandding')
    status_picture = ResizedImageField(size=[450, 450], crop=['middle', 'center'],
                                upload_to="Complaint_Picture", null=True,blank=True)
    
    
    def __str__(self):
        return str(self.user)
    

    
    
    