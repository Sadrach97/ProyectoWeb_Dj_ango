from django.shortcuts import render,redirect
from .models import Cliente,Producto,Carrito
from django.db.models import Sum
from django.contrib import messages
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
    Correo = request.POST['Correo']
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
    plantilla = Producto.object.get(idProducto=45)
    contexto = {"pantilla":plantilla}
    return render(request, 'plantilla.html',contexto)
def children(request):
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
    return render(request, 'carrito.html',contexto)
def iniciar(request):
    return render(request, "logeado.html")



def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(Email=request.POST['correo'], pwd=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['Email']=detalleUsuario.Email
            return render(request, 'index.html')
        except nuevoUsuario.doesNotExist as e:
            messages.success(request, 'Nombre de usuario o Password no es correcto..!')
    return render(request, 'Login.html')
def carr(request):
    car = Carrito.objects.all()
    precio = Carrito.precio
    total = Carrito.objects.annotate(Total=Sum(precio))
    texto = {"carri":car}
    return render(request, 'carrito.html',texto)


def cerrarSesion(request):
    try:
        del request.session['correo']
    except:
        return render(request, 'Menu.html')
    return render(request, 'Menu.html')
