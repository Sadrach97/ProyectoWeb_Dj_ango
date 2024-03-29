from zlib import DEF_BUF_SIZE
from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True,verbose_name="Id Cliente")
    nombre = models.CharField(max_length=20,verbose_name="Nombre Cliente",blank=False,null=False)
    apellido = models.CharField(max_length=20,verbose_name="Apellido Cliente",blank=False,null=False)
    telefono = models.IntegerField(verbose_name="Telefono Cliente")
    correo = models.CharField(max_length=40,verbose_name="Correo Cliente",blank=False,null=False,unique=True)
    contraseña = models.CharField(max_length=12,verbose_name="Contraseña1",blank=False,null=False)
    scontraseña = models.CharField(max_length=12,verbose_name="Contraseña2",blank=False,null=False)
    
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="Id Producto")
    nombreProducto = models.CharField(max_length=20,verbose_name="Nombre Producto",blank=False,null=False)
    modelo = models.CharField(max_length=20,verbose_name="Modelo zapatilla",blank=False,null=False)
    precio = models.IntegerField(verbose_name="Precio",blank=False,null=False)
    fotoProducto = models.ImageField(upload_to="zapatilla",blank=False,null=False)
    descripcion = models.CharField(max_length=100,verbose_name="Descripcion",blank=False,null=False)

    def __str__(self):
        return self.nombreProducto

class Carrito(models.Model):
    idProducto = models.IntegerField(primary_key=True,verbose_name="Id Producto")
    nombreProducto = models.CharField(max_length=20,verbose_name="Nombre Producto",blank=False,null=False)
    precio = models.IntegerField(verbose_name="Precio",blank=False,null=False)

    def __str__(self):
        return self.nombreProducto

class DetalleCarrito(models.Model):
    idDetalle = models.AutoField(primary_key=True,verbose_name="Id Detalle")
    idProd = models.IntegerField(verbose_name="Id del producto")
    idclie = models.IntegerField(verbose_name="Id del Cliente")
    nombrePo = models.CharField(max_length=100,verbose_name="Nombre del Producto",blank= False,null= False)

    def __str__(self):
        return self.idDetalle

