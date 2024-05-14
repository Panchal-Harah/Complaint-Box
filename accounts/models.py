from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django_resized import ResizedImageField


# Create your models here.

GENDER_CHOICES = (
    ('--Select Gender--','--Select Gender--'),
    ('M', 'Male'),
    ('F', 'Female')
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

# STATUS_CHOICES = (
#     ('pending', 'pending'),
#     ('approval', 'approval')
# )



class cuser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.user)

class employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.user)
    

class Profile(models.Model):
    user = models.OneToOneField(cuser, on_delete=models.PROTECT, primary_key=True)
    tel = models.IntegerField(default=None, null=True)
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, default='--Select Gender--')
    city = models.CharField(
        max_length=50, choices=CITY_CHOICES, default='--Select City--')
    age = models.IntegerField(default=18, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=200, null=True,blank=True)
    join_date = models.DateField(auto_now_add=True)
    # profile_pic = models.ImageField(upload_to="Profile_pic", null=True,blank=True, default="/Profile_pic/avatar_2x.png")
    profile_pic = ResizedImageField(size=[450, 450], crop=['middle', 'center'],upload_to="Profile_pic", null=True,blank=True, default="/Profile_pic/undraw_Pic_profile_re_7g2h.png")

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=cuser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=cuser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Employee


class Employee_Profile(models.Model):
    user = models.OneToOneField(employee, on_delete=models.PROTECT, primary_key=True)
    tel = models.IntegerField(default=None, null=True)
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, default='--Select Gender--')
    city = models.CharField(
        max_length=50, choices=CITY_CHOICES, default='--Select City--')
    age = models.IntegerField(default=18, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=200, null=True,blank=True)
    join_date = models.DateField(auto_now_add=True)
    # profile_pic = models.ImageField(upload_to="Profile_pic", null=True,blank=True, default="/Profile_pic/avatar_2x.png")
    profile_pic = ResizedImageField(size=[450, 450], crop=['middle', 'center'],upload_to="Profile_pic", null=True,blank=True, default="/Employee_Profile_pic/undraw_Pic_profile_re_7g2h.png")
    # status = models.CharField(
    #     max_length=50, choices=STATUS_CHOICES, default='pending', null=True, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=employee)
def create_user_Employee_Profile(sender, instance, created, **kwargs):
    if created:
        Employee_Profile.objects.create(user=instance)

@receiver(post_save, sender=employee)
def save_employee_profile(sender, instance, **kwargs):
    instance.employee_profile.save()
    
    