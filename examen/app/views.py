import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .forms import ContactoForm

# Create your views here.

class Productos(APIView):
    def get(self, request):
        nombre = request.GET.get('nombre')
        return Response({'message': 'Listado de Productos '+nombre})
    def post(self, request):
        if ("nombre","descripcion","precio" in request.data):
            nombre = request.data.get('nombre')
            precio = request.data.get('precio')
            descripcion = request.data.get('descripcion')
            return Response({'message': 'Producto creado ','nombre':nombre,'precio':precio,'descripcion':descripcion})
        else:
            return Response({'message': 'No se recibieron datos'})

class TipoProducto(APIView):
    def post(self, request):
        if ("nombre" in request.data):
            nombre = request.data.get('nombre')
            tipoObjeto = TIPO_PRODUCTO()
            tipoObjeto.nombre = nombre
            tipoObjeto.save()
            return Response({'message': 'Tipo de Producto creado','nombre':nombre, 'id':tipoObjeto.id_tipo_producto})
        else:
            return Response({'message': 'No se recibieron datos'})
    def get(self, request):
        producto = TIPO_PRODUCTO.objects.all().values()
        return Response({producto})
    def put(self, request):
        if ("id","nombre" in request.data):
            id = request.data.get('id')
            nombre = request.data.get('nombre')
            try:
                tipoObjeto = TIPO_PRODUCTO.objects.get(id_tipo_producto=id)
                tipoObjeto.nombre = nombre
                tipoObjeto.save()
                return Response({'message': 'Tipo de Producto actualizado','nombre':nombre, 'id':tipoObjeto.id_tipo_producto})
            except TIPO_PRODUCTO.DoesNotExist:
                return Response({'message': 'id de ese tipo de producto no existe'})
        else:
            return Response({'message': 'No se recibieron datos'})
    def delete(self, request):
        if ("id" in request.data):
            id = request.data.get('id')
            try:
                tipoObjeto = TIPO_PRODUCTO.objects.get(id_tipo_producto=id)
                nombre = TIPO_PRODUCTO.objects.get(id_tipo_producto=id).nombre
                tipoObjeto.delete()
                return Response({'message': 'Tipo de Producto eliminado','id':id ,'nombre':nombre})
            except TIPO_PRODUCTO.DoesNotExist:
                return Response({'message': 'id de ese tipo de producto no existe'})
        else:
            return Response({'message': 'No se recibieron datos'})



def home(request):
    productos = PRODUCTOS.objects.all()
    mascotas = TIPO_MASCOTA.objects.all()
    data = {
        'productos': productos,
        'mascotas': mascotas
        }
    return render(request, 'app/home.html', data)

def register(request):
    return render(request, 'app/register.html')

def about(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'app/sobrenosotros.html', data)

def productos(request):
    return render(request, 'app/productos.html')