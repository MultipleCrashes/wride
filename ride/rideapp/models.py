from django.db import models

# Create your models here.


import uuid


class User(models.Model):
    user_id = models.CharField(max_length=10000,null=True,blank=True)
    first_name = models.CharField(max_length=1000,null=True,blank=True)
    last_name = models.CharField(max_length=1000,null=True,blank=True)



class Bill(models.Model):
    bill_id = models.CharField(max_length=10000,null=True,blank=True)
    bill_details = models.CharField(max_length=10000,null=True,blank=True)
    total_bill = models.CharField(max_length=10000,null=True,blank=True)


class Simplify(models.Model):
    bill_id = models.CharField(max_length=10000,null=True,blank=True)
    bill_details = models.CharField(max_length=10000,null=True,blank=True)
    total_bill = models.CharField(max_length=10000,null=True,blank=True)