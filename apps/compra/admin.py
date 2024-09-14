from django.contrib import admin

from .models import Proveedore, Compra, Detallecompra

# Register your models here.
admin.site.register(Proveedore)
admin.site.register(Compra)
admin.site.register(Detallecompra)
