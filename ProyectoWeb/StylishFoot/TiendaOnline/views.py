from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'Menú.html')

def inicio1(request):
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
