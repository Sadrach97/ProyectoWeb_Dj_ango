from django.contrib import admin
from django.urls import path
from .views import inicio,inicio1,registrar,registroR,logeado,inicio2

urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio',inicio1,name="inicio logo"),
    path('register',registrar,name="registrar"),
    path('registrado',registroR,name="registradoP"),
    path('logeado',logeado,name="logeado"),
    path('inicio2',inicio2,name="inicio logo2"),
]