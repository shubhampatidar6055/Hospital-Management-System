from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path("admin_login/",admin_login),
    path("login/",login),
    path("admin_signup/",admin_signup),
    path("admin_data/",admin_data),
    path("admin_view/", admin_view),
    path("appointment/",appointment),
    path("appointment_data/",appointment_data),
    path("delete_patient/<int:pk>/", delete_patient, name ="delete_patient"),
    path("delete_patient_admin/<int:pk>/", delete_patient_admin, name="delete_patient_admin"),
    path("doctor_login/", doctor_login),
    path("dr_login_data/", dr_login_data),
    path("doctor_register/",doctor_register),
    path("doctor_data/",doctor_data),
    path("update_doctor/<int:uid>/", update_doctor, name="update_doctor"),
    path("update_doctor_data/", update_doctor_data),
    path("delete_doctor/<int:pk>/", delete_doctor, name="delete_doctor"),
    path("patient_list/",patient_list),
    path("mail/",mail),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
