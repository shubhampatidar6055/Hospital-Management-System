from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,"index.html")

def admin_login(request):
    return render(request,"admin-login.html")

def login(request):
    if request.method == "POST":
        admin = Admin.objects.get(email=request.POST['email'])
        if check_password(request.POST['password'],admin.password):
            request.session['login'] = True
            request.session['email'] = admin.email
            return redirect('/admin_view/')
        else:
            messages.error(request,"Invalid Id Password")
            return redirect("/admin_view/")

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
            return redirect("/admin_view/")
        
def admin_view(request):
    doctor_obj = Doctor.objects.all()
    patient_obj = Appointment.objects.all()
    return render(request, "admin-view.html", {"patient_obj":patient_obj, "doctor_obj":doctor_obj})

def appointment(request):
    doctor_obj = Doctor.objects.all()
    return render(request,"appointment.html", {"doctor_obj":doctor_obj})

def appointment_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        ap_date = request.POST.get('ap_date')
        address = request.POST.get('address')
        report = request.FILES.get('report')
        d_name = request.POST.get('dr_name')
        n_name = Doctor.objects.get(id=d_name)
        if Appointment.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exists")
        elif Appointment.objects.filter(mobile_no=mobile_no).exists():
            messages.error(request, "Mobile Number Already Register")
        else:
            Appointment.objects.create(name=name, mobile_no=mobile_no, email=email,gender
                                       =gender, dob=dob, ap_date=ap_date, address=address,
                                        report=report, dr_name=n_name)
            messages.success(request, "Appointment Booked Sucessfully")
            return redirect("/appointment/")
        
def delete_patient(request,pk):
    Appointment.objects.get(id=pk).delete()
    return redirect("/patient_list/")

def delete_patient_admin(request,pk):
    Appointment.objects.get(id=pk).delete()
    return redirect("/admin_view/")

def doctor_login(request):
    return render(request, "doctor-login.html")

def dr_login_data(request):
    if request.method == "POST":
        admin = Doctor.objects.get(email=request.POST['email'])
        if check_password(request.POST['password'],admin.password):
            request.session['login'] = True
            request.session['email'] = admin.email
            return redirect('/admin_signup/')
        else:
            messages.error(request,"Invalid Id Password")
            return redirect("/patient_list/")

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
    
def delete_doctor(request,pk):
    Doctor.objects.get(id=pk).delete()
    return redirect("/admin_view/")
    
def patient_list(request):
    patient_obj = Appointment.objects.all()
    return render(request,"patient-list.html", {"patient_obj":patient_obj}) 

def mail(request):   
    send_mail(
    "Testing",
    "Appointment Successfull.",
    "shubhampatidar6055@gmail.com",
    ["shubhamgothi6055@gmail.com"],
    fail_silently=False,
)