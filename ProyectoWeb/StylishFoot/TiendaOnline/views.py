from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'Menú.html')

def inicio1(request):
    return render(request,'Menú.html')

def inicio2(request):
    return render(request,'Menú.html')

def registrar(request):
    return render(request,'Register.html')

def registroR(request):
    NombreP = request.POST['nom']
    Apellido = request.POST['appate']
    Telefono = request.POST['telefono']
    Correo = request.POST['Correo']
    Contraseña1 = request.POST['clave1']
    Contraseña2 = request.FILES['clave2']

def logeado(request):
    return render(request,'logeado.html')

def editar(request):
    return render(request,'Editar_perfil.html')

def admin(request):
    return render(request, 'menu_admin.html')
def hombre(request):
    return render(request, 'hombree.html')
def mujer(request):
    return render(request, 'mujer.html')
def children(request):
    return render(request, 'children.html')