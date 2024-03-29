from django.shortcuts import render,redirect
from .models import Cliente,Producto,Carrito,DetalleCarrito
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def inicio(request):
    productos = Producto.objects.all()
    cot = {"prod":productos}
    return render(request,'Menú.html',cot)

def inicio1(request):
    productos = Producto.objects.all()
    cot = {"prod":productos}
    return render(request,'Menú.html',cot)

def inicio2(request):
    productos = Producto.objects.all()
    cot = {"prod":productos}
    return render(request,'Menú.html',cot)

def register(request):
    return render(request,'Register.html')
    

def registroR(request):
    NombreP = request.POST['nom']
    Apellido = request.POST['appate']
    Telefono = request.POST['telefono']
    Correo = request.POST['Correo1']
    Contraseña1 = request.POST['clave1']
    Contraseña2 = request.POST['clave2']
    

    Cliente.objects.create(nombre=NombreP,apellido=Apellido,telefono=Telefono,correo=Correo,contraseña=Contraseña1,scontraseña=Contraseña2)
    return redirect('logeado')

def Login(request):
    return render(request,'Login.html')

def logeado(request):
    
    productos = Producto.objects.all()
    cot = {"prod":productos}
    return render(request,'logeado.html',cot)

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
        clientes = Cliente.objects.all()
        cot = {"cli":clientes}
        return render(request, 'Editar_perfil.html',cot)


def producto(request):
    return render(request, 'plantilla.html')
def children(request):
    cr = Cliente.objects.all()
    conte = {"cle":cr}
    return render(request, 'plantillaZapato.html')
def Agregar(request):
    return render(request, 'AgregarP.html')
def MenuA(request):
    productos = Producto.objects.all()
    cot = {"prod":productos}
    return render(request, 'login_admin.html',cot)
def registroP(request):
    Nombre = request.POST['nomP']
    Modelo = request.POST['modelo']
    Precio = request.POST['precio']
    Foto = request.FILES['foto']
    Descripcion = request.POST['descrip']
    

    Producto.objects.create(nombreProducto=Nombre,modelo=Modelo,precio=Precio,fotoProducto=Foto,descripcion=Descripcion)
    return redirect('MenuA')
def eliminar_P(request,id):
    producto1 = Producto.objects.get(idProducto = id)
    producto1.delete() #elimina el registro

    return redirect('MenuA')
def ListaP(request):
    productos = Producto.objects.all()
    cot = {"prod":productos}
    return render(request, 'ListaP.html',cot)
def modificar_P(request,id):
    producto2 = Producto.objects.get(idProducto = id)
    contexto = {
        "producto" : producto2
    }
    return render(request, 'modificacion.html',contexto)
def modificaciones_P(request,id):
    nombre_p = request.POST['nombre_P']
    precio1 = request.POST['precio']
    modelo1 = request.POST['modelo']
    foto1 = request.FILES['foto']
    descrip1 = request.POST['descrip']

    nombre1 = Producto.objects.get(idProducto= id) #el registro original
    #comienzo a reemplazar los valores en ese registro original
    nombre1.nombreProducto = nombre_p
    nombre1.precio = precio1
    nombre1.modelo = modelo1
    nombre1.fotoProducto = foto1
    nombre1.descripcion = descrip1

    nombre1.save() #update
    return redirect('MenuA')
def carrito(request):
    return render(request, 'carrito.html')
def agregar(request,id):
    producto2 = Producto.objects.get(idProducto=id)
    i = producto2.idProducto
    nom = producto2.nombreProducto
    pre = producto2.precio
    Carrito.objects.create(idProducto=i,nombreProducto=nom,precio=pre)
    return redirect('inicio')
def quitar(request,id):
    producto3 = Producto.objects.all()
    return render(request, 'carrito.html')
def iniciar(request):
    return render(request, "logeado.html")



def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleUsuario=Cliente.objects.get(correo=request.POST['correo'], contraseña=request.POST['contraseña'])
            print("Cliente=", detalleUsuario)
            if detalleUsuario.correo == "Admin@stylish.foot":
                return redirect('MenuA')
            else:
                return redirect('logeado')
        except Cliente.DoesNotExist as e:
            messages.success(request, 'Nombre de usuario o Contraseña no es correcto..!')
    return render(request, 'Login.html')
def carr(request):
    car = Carrito.objects.all()
    texto = {"carri":car}
    return render(request, 'carrito.html',texto)


def cerrarSesion(request):
    try:
        del request.session['correo']
    except:
        return render(request, 'Menu.html')
    return render(request, 'Menu.html')

def traer(request,id):
    numero = Cliente.objects.get(idCliente = id)
    pro = {'Client':numero}
    return render(request, 'plantillaZapato.html',pro)
def carr1(request):
    car = Carrito.objects.all()
    precio = Carrito.precio
    total = Carrito.objects.annotate(Total=Sum(precio))
    texto = {"carri":car}
    return render(request, 'carrito copy.html',texto)

def admin3(request):
    ad = User.objects.all()
    cont = {"todo":ad}
    return render(request,'admin.html',cont)
def borrar(request,id):
    producto3 = Carrito.objects.get(idProducto = id)
    producto3.delete() #elimina el registro

    return redirect('carr')

def agregar1(request,id):
    producto2 = Producto.objects.get(idProducto=id)
    i = producto2.idProducto
    nom = producto2.nombreProducto
    pre = producto2.precio
    Carrito.objects.create(idProducto=i,nombreProducto=nom,precio=pre)
    return redirect('logeado')

def borrar1(request,id):
    producto3 = Carrito.objects.get(idProducto = id)
    producto3.delete() #elimina el registro

    return redirect('carr1')