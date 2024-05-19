from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",admin_login),
    path("admin_signup/",admin_signup),
    path("admin_data/",admin_data),
    path("appointment/",appointment),
    path("doctor_register/",doctor_register),
]
