from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    licencia = models.CharField(max_length=255)
    fechaini = models.DateField()
    fechafin = models.DateField()
    logo = models.ImageField(upload_to='empresas/', max_length=200, blank=True, null=True)
    about = models.CharField(max_length=100, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Sucursale(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ipsucursal = models.CharField(max_length=15)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING )
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Configuracione(models.Model):
    utilidadactive = models.BooleanField()
    utilidad = models.IntegerField(blank=True, null=True)
    ivaactive = models.BooleanField()
    iva = models.IntegerField(blank=True, null=True)
    sucursal = models.ForeignKey(Sucursale, on_delete=models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.sucursal
    
class CorrelativoFact(models.Model):
    
    TICKET = 'TICKET'
    FACTURA = 'FACTURA'
    CREDITO_FISCAL = 'CREDITO FISCAL'
    TIPO_DOCUMENTO_CHOICES = (
		(TICKET, 'TICKET'),
		(FACTURA, 'FACTURA'),
        (CREDITO_FISCAL, 'CREDITO FISCAL')
	)
    correlativoini = models.CharField(max_length=100)
    correlativofin = models.CharField(max_length=100)
    tipodocumento = models.CharField(null=True, blank=True, max_length=15, choices = TIPO_DOCUMENTO_CHOICES)
    numdocumentoasig = models.CharField(max_length=50)
    fechadocumento = models.DateField()
    correlativoact = models.CharField(max_length=50)
    sucursal = models.ForeignKey(Sucursale, on_delete=models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usercreate = models.CharField(max_length=20)
    usermodify = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.sucursal
