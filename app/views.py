from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

def admin_login(request):
    return render(request,"admin-login.html")

def admin_signup(request):
    return render(request,"admin-signup.html")

def admin_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        password = make_password(request.POST.get('password'))
        if Admin.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists")
            return redirect("/admin_signup/")
        else:
            Admin.objects.create(name=name, email=email, mobile_no=mobile_no,
                                  password=password)
            return redirect("//")

def appointment(request):
    return render(request,"appointment.html")

def doctor_register(request):
    return render(request,"doctor-register.html")