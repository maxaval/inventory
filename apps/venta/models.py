from email.policy import default
from random import choice, choices
from django.db import models

from apps.inventario.models import Producto
from apps.configuracion.models import Sucursale

# Create your models here.
class Apertura(models.Model):
    
    ESTADO_APERTURA_CHOICES = (
        ('ABIERTA', 'Abierta'),
        ('CERRADA', 'Cerrada'),
        # Puedes agregar más opciones aquí
    )
    
    concepto = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    horaopen = models.TimeField()
    horaclose = models.TimeField(blank=True, null=True)
    fondocaja = models.DecimalField(max_digits=10, decimal_places=4)
    fondopago = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    totalcierre = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_APERTURA_CHOICES)
    sucursal = models.ForeignKey(Sucursale, models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.concepto
    
class Venta(models.Model):
    
    ESTADO_VENTA_CHOICES = (
        ('PAGADA', 'Pagada'),
        ('ANULADA', 'Anulada'),
        ('CREDITO 30', 'Crédito 30'),
        # Puedes agregar más opciones aquí
    )
    
    factura = models.CharField(max_length=50, blank=True)
    cliente = models.CharField(max_length=100)
    insumo = models.IntegerField(blank=True, null=True)
    totalventa = models.DecimalField(max_digits=10, decimal_places=4)
    pago = models.DecimalField(max_digits=10, decimal_places=4)
    cambio = models.DecimalField(max_digits=10, decimal_places=4)
    estado = models.CharField(max_length=10, choices=ESTADO_VENTA_CHOICES)
    perdida = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)
    apertura = models.ForeignKey(Apertura, models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.factura + " - " + self.cliente

class Detalleventa(models.Model):
    cantidad = models.IntegerField()
    preciounitario = models.DecimalField(max_digits=10, decimal_places=4)
    totalproducto = models.DecimalField(max_digits=10, decimal_places=4)
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
