from django.db import models

# Create your models here.
class TIPO_PRODUCTO(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'TIPO_PRODUCTO'
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Producto'
        ordering = ['id_tipo_producto']

class TIPO_MASCOTA(models.Model):
    id_tipo_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'TIPO_MASCOTA'
        verbose_name = 'Tipo de Mascota'
        verbose_name_plural = 'Tipos de Mascotas'
        ordering = ['id_tipo_mascota']

class PRODUCTOS(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    tipo_producto = models.ForeignKey(TIPO_PRODUCTO, on_delete=models.PROTECT, null=True, blank=True)
    tipo_mascota = models.ForeignKey(TIPO_MASCOTA, on_delete=models.PROTECT, null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'PRODUCTOS'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

opciones_consulta = [
    [0,'consulta'],
    [1,'reclamo'],
    [2,'sugerencia'],
]

class CONTACTO(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    email = models.EmailField()
    avisos = models.BooleanField(default=False)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'CONTACTO'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['id']

