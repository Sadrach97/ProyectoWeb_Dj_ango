from django.contrib import admin
from django.urls import path

from .views import inicio,inicio1,register,registroR,logeado,inicio2,Editar_perfil,admin,hombre,mujer,children,datos,producto,Agregar,MenuA,registroP,eliminar_P,ListaP,modificaciones_P,modificar_P,carrito,agregar,quitar,iniciar,carr,paginaLogin,carr1,admin3,borrar




urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio',inicio1,name="inicio logo"),
    path('register',register,name="registrar"),
    path('registroR',registroR,name="registroR"),
    path('logeado',logeado,name="logeado"),
    path('inicio2',inicio2,name="inicio logo2"),
    path('Perfil',Editar_perfil,name="Editar_perfil"),
    path('admin1',admin,name="admin"),
    path('hombre',hombre,name="hombre"),
    path('mujer',mujer,name="mujer"),
    path('children',children,name="children"),
    path('d',datos,name="datos"),
    path('producto',producto,name="producto"),
    path('Agregar',Agregar,name="Agregar"),
    path('MenuA',MenuA,name="MenuA"),
    path('registroP',registroP,name="registroP"),
    path('eliminar/<int:id>',eliminar_P, name="eliminar_P"),
    path('ListaP',ListaP,name="ListaP"),
    path('modificar_P/<int:id>',modificar_P,name="modificar_P"),
    path('modificaciones_P/<int:id>',modificaciones_P,name="modificaciones_P"),
    path('carrito',carrito,name="carrito"),
    path('agregar/<int:id>',agregar,name="agregar"),
    path('quitar/<int:id>',quitar,name="quitar"),
    path('iniciar',iniciar,name="iniciar"),
    path('carr',carr,name="carr"),
    path('paginaLogin',paginaLogin,name="paginaLogin"),
    path('carr1',carr1,name="carr1"),
    path('admin3',admin3,name="admin3"),
    path('borrar/<int:id>',borrar, name="borrar"),
]    
