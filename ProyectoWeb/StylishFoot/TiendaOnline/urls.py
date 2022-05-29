from django.contrib import admin
from django.urls import path
from .views import inicio,inicio1,registrar

urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio',inicio1,name="inicio logo"),
    path('register',registrar,name="registrar"),
]