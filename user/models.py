from django.db import models
from django_resized import ResizedImageField
from accounts.models import *
# Create your models here.

COMPLAINT_CHOICES = (
    ('--Complaint Type--', '--Complaint Type--'),
    ('Street Light', 'Street Light'),
    ('Pipe Leakage', 'Pipe Leakage'),
    ('Rainwater Drainage', 'Rainwater Drainage'),
    ('Road Reconstruction', 'Road Reconstruction'),
    ('Garbage System', 'Garbage System')
)

CITY_CHOICES = (
    ('--Select City--','--Select City--'),
    ('Ahmedabad','Ahmedabad'),
    ('Gandhinagar','Gandhinagar'),
    ('Surat','Surat'),
    ('Rajkot','Rajkot'),
    ('Vadodara','Vadodara'),
    ('Bhavnagar','Bhavnagar'),
    ('Junagadh','Junagadh'),
    ('Jamnagar','Jamnagar')
)

GENDER_CHOICES = (
    ('--Select Gender--','--Select Gender--'),
    ('Male', 'Male'),
    ('Female', 'Female')
)


OPINION_CHOICES =(
    ('YES', 'YES'),
    ('NO', 'NO'),
    ('CAN NOT SAY', 'CAN NOT SAY')
)




class Complaint_Model(models.Model):
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    complaint_type = models.CharField(
         max_length=250, choices=COMPLAINT_CHOICES, default='--Complaint Type--')
    date = models.DateField()
    pincode = models.IntegerField()
    complaint_picture = ResizedImageField(size=[450, 450], crop=['middle', 'center'],
                                upload_to="Complaint_Picture", null=True,blank=True)
    
   
    
    def __str__(self):
        return str(self.username)

   
class Opinion_Model(models.Model):
    user = models.ForeignKey(cuser,on_delete=models.CASCADE,null=True,blank=True)
    redio = models.CharField(max_length=40,choices=OPINION_CHOICES, default="YES")
    text = models.TextField(max_length=500, null=True, blank=True)
        
    def __str__(self):
        return str(self.user.user)
    

