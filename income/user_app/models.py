from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class reg_insert(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)


class addincome(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=10)
    item = models.CharField(max_length=20)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class addexpense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=10)
    item = models.CharField(max_length=20)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
