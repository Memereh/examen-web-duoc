from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'stock', 'imagen', 'tipo_producto', 'tipo_mascota', 'descripcion']
    list_editable = ['precio', 'stock', 'descripcion']
    search_fields = ['nombre', 'descripcion']
    list_filter = ['tipo_producto', 'tipo_mascota']
    list_per_page = 5
    list_max_show_all: 10

class MascotaAdmin(admin.ModelAdmin):
    list_display = ['id_tipo_mascota', 'nombre', 'imagen']
    list_editable = ['nombre']



admin.site.register(TIPO_PRODUCTO)
admin.site.register(PRODUCTOS, ProductoAdmin)
admin.site.register(TIPO_MASCOTA, MascotaAdmin)
