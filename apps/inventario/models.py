import barcode, os
from barcode.writer import ImageWriter
from django.db import models
from PIL import Image

from django.conf import settings


from apps.configuracion.models import Sucursale

# Create your models here.    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    CAJA = 'CAJA'
    DOCENA = 'DOCENA'
    PAQUETE = 'PAQUETE'
    TIRA = 'TIRA'
    UNIDAD = 'UNIDAD'
    FARDO = 'FARDO'
    SACO = 'SACO'
    BOLSA = 'BOLSA'
    ARROBA = 'ARROBA'
    BLISTER = 'BLISTER'
    CONTENEDOR_CHOICES = (
		(CAJA, 'CAJA'),
		(DOCENA, 'DOCENA'),
        (PAQUETE, 'PAQUETE'),
        (TIRA, 'TIRA'),
		(UNIDAD, 'UNIDAD'),
        (FARDO, 'FARDO'),
        (SACO, 'SACO'),
		(BOLSA, 'BOLSA'),
        (ARROBA, 'ARROBA'),
        (BLISTER, 'BLISTER'),
	)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='productos/', max_length=255, blank=True, null=True)
    contenedor = models.CharField(null=True, blank=True, max_length=15, choices = CONTENEDOR_CHOICES)
    cantidadcontenedor = models.PositiveIntegerField(null=True, blank=True, default=0) 
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    def generar_codigo_barras(self):
        if self.codigo:
            code128 = barcode.Code128(self.codigo)

            # Asegúrate de que el directorio de uploads exista
            media_root = os.path.join(settings.MEDIA_ROOT, 'productos/barras')
            if not os.path.exists(media_root):
                os.makedirs(media_root)

            image_path = os.path.join(media_root, f'barcode_{self.id}.png') # type: ignore

            # Guardar la imagen en formato PNG
            code128.save(image_path, options={"write_text": False})

            # Devolver la ruta relativa de la imagen del código de barras
            return f'uploads/productos/barras/barcode_{self.id}.png.svg' # type: ignore

        return None

    
class Especiale(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20, blank=True, null=True)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.producto

class Inventario(models.Model):
    stock = models.PositiveBigIntegerField(blank=True, null=True)
    stockminimo = models.PositiveIntegerField(blank=True, null=True, default=0)
    stockmaximo = models.PositiveIntegerField(blank=True, null=True, default=0)
    preciocompra = models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)
    utilidad = models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)
    iva = models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)
    precioventa = models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)
    sucursal = models.ForeignKey(Sucursale, models.DO_NOTHING)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.producto
    