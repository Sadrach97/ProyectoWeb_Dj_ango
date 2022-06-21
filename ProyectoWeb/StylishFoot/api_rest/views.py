from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from TiendaOnline.models import Cliente
from .serializers import ClienteSerializers, ClienteSerializers2

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@csrf_exempt

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializers(clientes,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data1 = JSONParser().parse(request)
        serializer = ClienteSerializers(data = data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addCliente(request):
    data1 = JSONParser().parse(request)
    serializer = ClienteSerializers2(data = data1)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlarCliente(request,id):
    try:
        m = Cliente.objects.get(idCliente = id)
    except Cliente.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClienteSerializers2(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ClienteSerializers2(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
    