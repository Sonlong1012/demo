from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    age = models.IntegerField(default=0, null=True)
    salary = models.IntegerField(default=0, null=True)
    image = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=128,default=make_password("default_password"))
    # confirm_password = models.CharField(max_length=128)


