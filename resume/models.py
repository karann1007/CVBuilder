from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False,blank=False)
    school = models.CharField(max_length=50,null=False,blank=False)
    score = models.FloatField(null=False,blank=False)
    start_date = models.DateField(null=False,blank=False)
    end_date = models.DateField(null=False,blank=False)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False,blank=False)
    rating = models.IntegerField(null=False,blank=False)


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100,blank=False,null=False)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    phone = models.CharField(max_length=10,null=False,blank=False)
    street = models.TextField(max_length=100,null=False,blank=False)
    city = models.TextField(max_length=100,null=False,blank=False)
    state = models.TextField(max_length=100,null=False,blank=False)
    country = models.TextField(max_length=100,null=False,blank=False)
    pincode = models.IntegerField(null=False,blank=False)
    about = models.CharField(max_length=100,null=False,blank=False)
    previous_work = models.TextField(max_length=100,null=True,blank=True)
    projects = models.TextField(max_length=100,null=True,blank=True)
    extra_curricular = models.TextField(max_length=100,null=True,blank=True)

