from django.urls import path
from api_rest.views import listado_clientes,addCliente,controlarCliente
from api_rest.viewsLogin import login

urlpatterns = [
    path('listado_clientes/',listado_clientes,name="listado_clientes"),
    path('addCliente/',addCliente,name="addCliente"),
    path('controlarCliente/<int:id>',controlarCliente,name="controlarCliente"),
    path('login/',login,name="login"),
]
