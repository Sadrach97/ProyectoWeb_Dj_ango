from django.shortcuts import render,redirect
from .models import Cliente,Producto
# Create your views here.
def inicio(request):
    return render(request,'Menú.html')

def inicio1(request):
    return render(request,'Menú.html')

def inicio2(request):
    return render(request,'Menú.html')

def register(request):
    return render(request,'Register.html')


def registroR(request):
    NombreP = request.POST['nom']
    Apellido = request.POST['appate']
    Telefono = request.POST['telefono']
    Correo = request.POST['Correo']
    Contraseña1 = request.POST['clave1']
    Contraseña2 = request.POST['clave2']

    Cliente.objects.create(nombre=NombreP,apellido=Apellido,telefono=Telefono,correo=Correo,contraseña=Contraseña1,scontraseña=Contraseña2)
    return redirect('logeado')

def logeado(request):
    return render(request,'logeado.html')

def Editar_perfil(request):
    return render(request,'Editar_perfil.html')

def admin(request):
    return render(request, 'menu_admin.html')
def hombre(request):
    return render(request, 'hombree.html')
def mujer(request):
    return render(request, 'mujer.html')
def children(request):
    return render(request, 'children.html')
def datos(request):
    NombreU = request.POST['nom']
    Apellido1 = request.POST['appate']
    Telefono1 = request.POST['telefono']
    Correo1 = request.POST['Correo']
    Contraseña2 = request.POST['clave1']
    Contraseña3 = request.POST['clave2']

    cliente = Cliente.objects.get(nombre=NombreU)

def producto(request):
    contexto = {"nombreProducto":"Tacones","modelo":"Zapatos de Mujer"}
    return render(request, 'plantilla.html',contexto)
def children(request):
    return render(request, 'plantillaZapato.html')
def Agregar(request):
    return render(request, 'AgregarP.html')
def MenuA(request):
    return render(request, 'login_admin.html')
def registroP(request):
    Nombre = request.POST['nomP']
    Modelo = request.POST['modelo']
    Precio = request.POST['precio']
    Foto = request.FILES['foto']
    Descripcion = request.POST['descrip']
    

    Producto.objects.create(nombreProducto=Nombre,modelo=Modelo,precio=Precio,fotoProducto=Foto,descripcion=Descripcion)
    return redirect('MenuA')