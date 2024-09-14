from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Empresa, Sucursale, Configuracione, CorrelativoFact
from .forms import EmpresaForm, SucursaleForm, ConfiguracioneForm, CorrelativoFactForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.urls import reverse_lazy

# Create your views here.

class EmpresaList(ListView):
    model = Empresa
    template_name = 'configuracion/empresalist.html'

class EmpresaCreate(BSModalCreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'configuracion/empresaadd.html'
    success_message = 'Hecho! Empresa Creada Correctamente.'
    success_url = reverse_lazy('configuracion:empresalist')

class EmpresaUpdate(BSModalUpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'configuracion/empresaedit.html'
    success_message = 'Hecho! Empresa Actualizada Correctamente.'
    success_url = reverse_lazy('configuracion:empresalist')

class EmpresaDelete(BSModalDeleteView):
    model = Empresa
    template_name = 'configuracion/empresadelete.html'
    success_message = 'Hecho! Empresa Eliminada Correctamente.'
    success_url = reverse_lazy('configuracion:empresalist')
    
#####################################################################################################3

class SucursaleList(ListView):
    model = Sucursale
    template_name = 'configuracion/sucursallist.html'

class SucursaleCreate(BSModalCreateView):
    model = Sucursale
    form_class = SucursaleForm
    template_name = 'configuracion/sucursaladd.html'
    success_message = 'Hecho! Sucursal Creada Correctamente.'
    success_url = reverse_lazy('configuracion:sucursallist')
    
class SucursaleUpdate(BSModalUpdateView):
    model = Sucursale
    form_class = SucursaleForm
    template_name = 'configuracion/sucursaledit.html'
    success_message = 'Hecho! Sucursal Actualizado Correctamente.'
    success_url = reverse_lazy('configuracion:sucursallist')

class SucursaleDelete(BSModalDeleteView):
    model = Sucursale
    template_name = 'configuracion/sucursaldelete.html'
    success_message = 'Hecho! Sucursal Eliminada Correctamente.'
    success_url = reverse_lazy('configuracion:sucursallist')
    
#######################################################################################################

class ConfiguracioneList(ListView):
    model = Configuracione
    template_name = 'configuracion/configuracionlist.html'
    
class ConfiguracioneCreate(BSModalCreateView):
    model = Configuracione
    form_class = ConfiguracioneForm
    template_name = 'configuracion/configuracionadd.html'
    success_message = 'Hecho! Configuración de Sucursal Creada Correctamente.'
    success_url = reverse_lazy('configuracion:configuracionlist')
    
class ConfiguracioneUpdate(BSModalUpdateView):
    model = Configuracione
    form_class = ConfiguracioneForm
    template_name = 'configuracion/configuracionedit.html'
    success_message = 'Hecho! Configuración de Sucursal Actualizada Correctamente.'
    success_url = reverse_lazy('configuracion:configuracionlist')

class ConfiguracioneDelete(BSModalDeleteView):
    model = Configuracione
    template_name = 'configuracion/configuraciondelete.html'
    success_message = 'Hecho! Configuración de Sucursal Eliminada Correctamente.'
    success_url = reverse_lazy('configuracion:configuracionlist')
    
######################################################################################################    

class CorrelativoFactList(ListView):
    model = CorrelativoFact
    template_name = 'configuracion/correlativolist.html'
    
class CorrelativoFactCreate(BSModalCreateView):
    model = CorrelativoFact
    form_class = CorrelativoFactForm
    template_name = 'configuracion/correlativoadd.html'
    success_message = 'Hecho! Correlativo de Documentos para la Sucursal Creada Correctamente.'
    success_url = reverse_lazy('configuracion:correlativolist')
    
class CorrelativoFactUpdate(BSModalUpdateView):
    model = CorrelativoFact
    form_class = CorrelativoFactForm
    template_name = 'configuracion/correlativoedit.html'
    success_message = 'Hecho! Correlativo de Documentos para la Sucursal Actualizada Correctamente.'
    success_url = reverse_lazy('configuracion:correlativolist')

class CorrelativoFactDelete(BSModalDeleteView):
    model = CorrelativoFact
    template_name = 'configuracion/correlativodelete.html'
    success_message = 'Hecho! Correlativo de Documentos para la Sucursal Eliminada Correctamente.'
    success_url = reverse_lazy('configuracion:correlativolist')
