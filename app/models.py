from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=150)
