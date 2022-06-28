from django.urls import path
from api_rest.views import listado_clientes,addCliente,controlarCliente,listado_producto,addProducto,controlarProducto
from api_rest.viewsLogin import login

urlpatterns = [
    path('listado_clientes/',listado_clientes,name="listado_clientes"),
    path('addCliente/',addCliente,name="addCliente"),
    path('controlarCliente/<int:id>',controlarCliente,name="controlarCliente"),
    path('listado_producto/',listado_producto,name="listado_producto/"),
    path('addProducto/',addProducto,name="addProducto"),
    path('controlarProducto/<int:id>',controlarProducto,name="controlarProducto"),
    path('login/',login,name="login"),
]
