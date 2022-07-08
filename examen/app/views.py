from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/sobrenosotros.html')

def productos(request):
    return render(request, 'app/productos.html')