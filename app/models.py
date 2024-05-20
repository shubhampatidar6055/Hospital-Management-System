from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=150)

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile_no = models.IntegerField()
    gender = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    Specialization = models.CharField(max_length=200)
    image = models.FileField()
    password = models.CharField(max_length=200)