from rest_framework import serializers
from TiendaOnline.models import Cliente,Producto

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['idCliente','nombre','apellido']


class ClienteSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['idCliente','nombre','apellido','telefono','correo','contraseña','scontraseña']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precio']


class ProductoSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','modelo','precio','descripcion']