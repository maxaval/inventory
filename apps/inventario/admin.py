from django.contrib import admin

from .models import Categoria, Producto, Especiale, Inventario

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Especiale)
admin.site.register(Inventario)