from email.policy import default
from random import choices
from django.db import models

from apps.inventario.models import Producto

# Create your models here.
class Proveedore(models.Model):
    nombre = models.CharField(max_length=100)
    representante = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    nit = models.CharField(max_length=14, blank=True, null=True)
    iva = models.CharField(max_length=14, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    
    ESTADO_COMPRA_CHOICES = (
        ('PAGADA', 'Pagada'),
        ('ANULADA', 'Anulada'),
        ('CREDITO 30', 'Crédito 30'),
        ('CREDITO 60', 'Crédito 60'),
        ('CREDITO 90', 'Crédito 90'),
        # Puedes agregar más opciones aquí
    )
    
    factura = models.CharField(max_length=15, blank=True)
    totalcompra = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    estado = models.CharField(max_length=10, choices = ESTADO_COMPRA_CHOICES)
    pagocaja = models.BooleanField(default=False)
    bonificacion = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)
    proveedor = models.ForeignKey(Proveedore, on_delete=models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.factura + " - " + self.proveedor # type: ignore

class Detallecompra(models.Model):
    cantidad = models.IntegerField()
    preciounitario = models.DecimalField(max_digits=10, decimal_places=4)
    preciototal = models.DecimalField(max_digits=10, decimal_places=4)
    compra = models.ForeignKey(Compra, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
