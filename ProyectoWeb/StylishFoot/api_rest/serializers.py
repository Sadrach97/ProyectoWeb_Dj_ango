from rest_framework import serializers
from TiendaOnline.models import Cliente

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['idCliente','nombre','apellido']


class ClienteSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['idCliente','nombre','apellido','telefono','correo','contraseña','scontraseña']
