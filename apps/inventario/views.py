from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Categoria, Producto, Especiale, Inventario
from .forms import CategoriaForm, ProductoForm, EspecialeForm, InventarioForm, CsvProcessorForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.urls import reverse_lazy, reverse
from .csv_processor import CsvProcessor
from django.apps import apps  
from django.http import JsonResponse, HttpResponseServerError, HttpResponseRedirect
from django.contrib import messages
from django import forms
import logging

# Create your views here.

class CategoriaList(ListView):
    model = Categoria
    template_name = 'inventario/categorialist.html'

class CategoriaCreate(BSModalCreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventario/categoriaadd.html'
    success_message = 'Hecho! Categoría Creada Correctamente.'
    success_url = reverse_lazy('inventario:categorialist')

class CategoriaUpdate(BSModalUpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventario/categoriaedit.html'
    success_message = 'Hecho! Categoría Actualizada Correctamente.'
    success_url = reverse_lazy('inventario:categorialist')

class CategoriaDelete(BSModalDeleteView):
    model = Categoria
    template_name = 'inventario/categoriadelete.html'
    success_message = 'Hecho! Categoría Eliminada Correctamente.'
    success_url = reverse_lazy('inventario:categorialist')
    
###################################################################################################

class ProductoList(ListView):
    model = Producto
    template_name = 'inventario/productolist.html'

class ProductoCreate(BSModalCreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/productoadd.html'
    success_message = 'Hecho! Producto Creado Correctamente.'
    success_url = reverse_lazy('inventario:productolist')

class ProductoUpdate(BSModalUpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/productoedit.html'
    success_message = 'Hecho! Producto Actualizado Correctamente.'
    success_url = reverse_lazy('inventario:productolist')

class ProductoDelete(BSModalDeleteView):
    model = Producto
    template_name = 'inventario/productodelete.html'
    success_message = 'Hecho! Producto Eliminado Correctamente.'
    success_url = reverse_lazy('inventario:productolist')
    
################################################################################################

class EspecialeList(ListView):
    model = Especiale
    template_name = 'inventario/especialelist.html'

class EspecialeCreate(BSModalCreateView):
    model = Especiale
    form_class = EspecialeForm
    template_name = 'inventario/especialeadd.html'
    success_message = 'Hecho! Producto Especial Creado Correctamente.'
    success_url = reverse_lazy('inventario:especialelist')

class EspecialeUpdate(BSModalUpdateView):
    model = Especiale
    form_class = EspecialeForm
    template_name = 'inventario/especialeedit.html'
    success_message = 'Hecho! Producto Especial Actualizado Correctamente.'
    success_url = reverse_lazy('inventario:especialelist')

class EspecialeDelete(BSModalDeleteView):
    model = Especiale
    template_name = 'inventario/especialedelete.html'
    success_message = 'Hecho! Producto Especial Eliminado Correctamente.'
    success_url = reverse_lazy('inventario:especialelist')
    
################################################################################################

class InventarioList(ListView):
    model = Inventario
    template_name = 'inventario/inventariolist.html'

class InventarioCreate(BSModalCreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/inventarioadd.html'
    success_message = 'Hecho! Producto Agregado al Inventario Correctamente.'
    success_url = reverse_lazy('inventario:inventariolist')

class InventarioUpdate(BSModalUpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/inventarioedit.html'
    success_message = 'Hecho! Producto Actualizado al Inventario Correctamente.'
    success_url = reverse_lazy('inventario:inventariolist')

class InventarioDelete(BSModalDeleteView):
    model = Inventario
    template_name = 'inventario/inventariodelete.html'
    success_message = 'Hecho! Producto Eliminado del Inventario Correctamente.'
    success_url = reverse_lazy('inventario:inventariolist')
    
#################################################################################################

def procesar_csv(request):
    try:
        if request.method == 'POST':
            form = CsvProcessorForm(request.POST, request.FILES)
            if form.is_valid():
                modelo_nombre = form.cleaned_data['modelo']
                modelo = apps.get_model('inventario', modelo_nombre)

                archivo = request.FILES['archivo']

                # Definir el mapeo de campos según el modelo seleccionado
                if modelo == Categoria:
                    field_mapping = {
                        'nombre': 'nombre',
                        'descripcion': 'descripcion',
                    }
                elif modelo == Producto:
                    field_mapping = {
                        'codigo': 'codigo',
                        'nombre': 'nombre',
                        'descripcion': 'descripcion',
                        'photo': 'photo',
                        'contenedor': 'contenedor',
                        'cantidadcontenedor': 'cantidadcontenedor',
                        'categoria_id': 'categoria_id',
                    }
                else:
                    # Agrega mapeos para otros modelos según sea necesario
                    field_mapping = {}

                csv_processor = CsvProcessor(model=modelo, csv_file=archivo, field_mapping=field_mapping)
                progreso = list(csv_processor.process_csv())

                # Agregar un mensaje de éxito
                messages.success(request, 'CSV procesado con éxito.')

            # Redirigir a la URL correspondiente
            if modelo == Categoria:
                return redirect('inventario:categorialist')
            elif modelo == Producto:
                return redirect('inventario:productolist')

    except Exception as e:
        # Capturar y registrar la excepción
        messages.error(request, f'Error al procesar el CSV: {str(e)}')
        return HttpResponseServerError()

    return render(request, 'inventario/procesarcsv.html', {'form': CsvProcessorForm()})
