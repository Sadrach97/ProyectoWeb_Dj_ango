from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'Menú.html')

def inicio1(request):
    return render(request,'Menú.html')

def registrar(request):
    return render(request,'Register.html')
