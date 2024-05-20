from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",admin_login),
    path("login/",login),
    path("admin_signup/",admin_signup),
    path("admin_data/",admin_data),
    path("appointment/",appointment),
    path("doctor_register/",doctor_register),
    path("doctor_data/",doctor_data),
    path("update_doctor/<int:uid>/", update_doctor, name="update_doctor"),
    path("update_doctor_data/", update_doctor_data),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
