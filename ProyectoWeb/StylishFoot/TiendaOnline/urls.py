from django.contrib import admin
from django.urls import path
from .views import inicio,inicio1,register,registroR,logeado,inicio2,editar,admin,hombre,mujer,children

urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio',inicio1,name="inicio logo"),
    path('register',register,name="registrar"),
    path('registroR',registroR,name="registroR"),
    path('logeado',logeado,name="logeado"),
    path('inicio2',inicio2,name="inicio logo2"),
    path('editar',editar,name="editar"),
    path('admin1',admin,name="admin"),
    path('hombre',hombre,name="hombre"),
    path('mujer',mujer,name="mujer"),
    path('children',children,name="children"),
]