from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)


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
    image = models.FileField(upload_to='doctor', max_length=100)
    password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Appointment(models.Model):
    name = models.CharField(max_length=150)
    mobile_no = models.IntegerField()
    email = models.EmailField(max_length=150)
    gender =models.CharField(max_length=150)
    dob = models.DateField()
    ap_date = models.DateField()
    dr_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    address = models.TextField()
    report = models.FileField(upload_to = 'patient', max_length=100)


    def __str__(self):
        return str(self.name)