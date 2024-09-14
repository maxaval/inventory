from django.contrib import admin

from .models import Apertura, Venta, Detalleventa

# Register your models here.
admin.site.register(Apertura)
admin.site.register(Venta)
admin.site.register(Detalleventa)
