from django.contrib import admin

from .models import Empresa, Sucursale, Configuracione, CorrelativoFact

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Sucursale)
admin.site.register(Configuracione)
admin.site.register(CorrelativoFact)
