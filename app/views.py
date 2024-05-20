from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

def admin_login(request):
    return render(request,"admin-login.html")

def login(request):
    if request.method == "POST":
        admin = Admin.objects.get(email = request.POST['email'])
        if check_password(request.POST['password'],admin.password):
            request.session['login'] = True
            request.session['email'] = Admin.email
            return redirect('/admin_signup/')
        else:
            messages.error(request,"Invalid Id Password")
            return redirect("/")

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
            return redirect("/admin_signup/")

def appointment(request):
    return render(request,"appointment.html")

def doctor_register(request):
    return render(request,"doctor-register.html")

def doctor_data(request):
    if request. method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        degree = request.POST.get('degree')
        experience = request.POST.get('experience')
        Specialization = request.POST.get('Specialization')
        image = request.FILES.get('image')
        password = make_password(request.POST.get('password'))
        if Doctor.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists")
            return redirect("/doctor_register/")
        else:
            Doctor.objects.create(name=name, email=email, mobile_no=mobile_no, gender=gender,
                                 dob=dob, address=address, degree=degree, experience=experience,
                                 Specialization=Specialization, image=image, password=password)
            return redirect("/doctor_register/")
        
def update_doctor(request,uid):
    doctor_obj = Doctor.objects.get(id=uid)
    return render(request, "update-doctor.html", {"doctor_obj":doctor_obj})

def update_doctor_data(request):
    if request. method == "POST":
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        degree = request.POST.get('degree')
        experience = request.POST.get('experience')
        Specialization = request.POST.get('Specialization')
        image = request.FILES.get('image')
        Doctor.objects.filter(id=uid).update(name=name, email=email, mobile_no=mobile_no, 
                                             gender=gender, dob=dob, address= address,
                                             degree=degree, experience=experience, Specialization
                                             =Specialization, image=image)
        return redirect("/doctor_register/")