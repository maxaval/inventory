from django.shortcuts import render, redirect
from .models import Compra, Detallecompra, Proveedore
from apps.configuracion.models import Configuracione
from apps.inventario.models import Inventario, Producto
from .forms import CompraForm, ProveedoreForm, DetalleCompraForm
from django.views.generic import ListView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView

# Create your views here.
class ProveedoreList(ListView):
    model = Proveedore
    template_name = 'compra/proveedorelist.html'
    
class ProveedoreCreate(BSModalCreateView):
    model = Proveedore
    form_class = ProveedoreForm
    template_name = 'compra/proveedoreadd.html'
    success_message = 'Hecho! Proveedor Creado Correctamente.'
    success_url = reverse_lazy('compra:proveedorelist')
    
class ProveedoreUpdate(BSModalUpdateView):
    model = Proveedore
    form_class = ProveedoreForm
    template_name = 'compra/proveedoreedit.html'
    success_message = 'Hecho! Proveedor Actualizado Correctamente.'
    success_url = reverse_lazy('compra:proveedorelist')

class ProveedoreDelete(BSModalDeleteView):
    model = Proveedore
    template_name = 'compra/proveedoredelete.html'
    success_message = 'Hecho! Proveedor Eliminado Correctamente.'
    success_url = reverse_lazy('compra:proveedorelist')
    
##########################################################################################

class CompraList(ListView):
    model = Compra
    template_name = 'compra/compralist.html'
    
class CompraCreate(BSModalCreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra/compraadd.html'
    success_message = 'Hecho! Compra Creada Correctamente.'
    
    def get_success_url(self):
        # Obtener el último objeto Compra creado
        ultima_compra = Compra.objects.latest('id')
        # Obtener el id de la última compra
        id_compra = ultima_compra.id # type: ignore
        # Redirigir a la vista de detalle de la última compra
        return reverse('compra:compraread', kwargs={'pk': id_compra})
    
class CompraRead(BSModalReadView):
    model = Compra
    template_name = 'compra/compradetalle.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detallecompras'] = Detallecompra.objects.filter(compra=self.object) # type: ignore
        return context

class CompraUpdate(BSModalUpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra/compraedit.html'
    success_message = 'Hecho! Compra Actualizada Correctamente.'
    success_url = reverse_lazy('compra:compralist')

class CompraDelete(BSModalDeleteView):
    model = Compra
    template_name = 'compra/compradelete.html'
    success_message = 'Hecho! Compra Eliminada Correctamente.'
    success_url = reverse_lazy('compra:compralist')
    
############################################################################################
    
class DetalleCompraList(ListView):
    model = Detallecompra
    template_name = 'compra/detallecompralist.html'
    
class DetalleCompraCreate(BSModalCreateView):
    model = Detallecompra
    form_class = DetalleCompraForm
    template_name = 'compra/detallecompraadd.html'
    success_message = 'Hecho! Detalle Creado Correctamente.'
    
    def get_success_url(self):
        return reverse('compra:compraread', kwargs={'pk': self.kwargs.get('compra_id')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compra_id'] = self.kwargs.get('compra_id')
        
        # Obtener la sucursal del usuario desde la sesión (asegúrate de tenerla guardada en la sesión)
        sucursal_id = self.request.session.get('sucursal')
        # Obtener configuración de la sucursal
        configuracion = get_object_or_404(Configuracione, sucursal_id=sucursal_id)
        if configuracion.utilidadactive is True:
            context['utilidadactive'] = configuracion.utilidadactive
        else:
            context['utilidadactive'] = False        
        
        # Obtener los valores de stock mínimo y máximo del producto
        producto_id = self.request.GET.get('producto')
        inventario = Inventario.objects.filter(producto_id=producto_id).first()
        if inventario:
            context['stockminimo'] = inventario.stockminimo
            context['stockmaximo'] = inventario.stockmaximo
            
        return context

    def form_valid(self, form):
        compra_id = self.kwargs.get('compra_id')
        producto_id = form.cleaned_data['producto'].id
        cantidad = form.cleaned_data['cantidad']
        preciototal = form.cleaned_data['preciototal']

        # Verificar si el producto ya existe en la compra
        if Detallecompra.objects.filter(compra_id=compra_id, producto_id=producto_id).exists():
            messages.error(self.request, 'El producto ya está en la compra.')
            return redirect('compra:compraread', pk=compra_id)

        # Si el producto no existe en la compra, proceder con la creación del detalle
        form.instance.compra_id = compra_id
        response = super().form_valid(form)
        
        # Obtener la sucursal del usuario desde la sesión (asegúrate de tenerla guardada en la sesión)
        sucursal_id = self.request.session.get('sucursal')
        
        # Obtener configuración de la sucursal
        configuracion = get_object_or_404(Configuracione, sucursal_id=sucursal_id)

        # Obtener detalles del producto
        producto = get_object_or_404(Producto, pk=producto_id)

        # Calcular cantidadtotal
        cantidadtotal = cantidad * producto.cantidadcontenedor

        # Calcular preciocompra
        preciocompra = preciototal / cantidadtotal

        # Calcular iva y utilidad
        iva = (preciocompra * configuracion.iva) / 100
        if configuracion.utilidadactive is True:
            utilidad = (preciocompra * configuracion.utilidad) / 100
            # Calcular precioventa
            precioventa = preciocompra + utilidad + iva
        else:            
            # Calcular precioventa
            precioventa = form.cleaned_data['precioventa']
            utilidad = precioventa - (preciocompra + iva)        
        
        # Crear o actualizar el objeto Inventario
        inventario, created = Inventario.objects.get_or_create(
            producto_id=producto_id,
            sucursal_id=sucursal_id,
            defaults={
                'stock': cantidadtotal,
                'preciocompra': preciocompra,
                'iva': iva,
                'utilidad': utilidad,
                'precioventa': precioventa,
                'stockminimo': form.cleaned_data['stockminimo'],
                'stockmaximo': form.cleaned_data['stockmaximo'],
                'usercreate': self.request.user.username,  # Usuario que crea el registro # type: ignore
                'usermodify': self.request.user.username   # Usuario que modifica el registro # type: ignore
            }
        )
        
        if not created:
            # Si ya existe el objeto Inventario, actualiza el stock sumando la cantidad del detalle
            inventario.stock += cantidad
            inventario.stockminimo = form.cleaned_data['stockminimo']
            inventario.stockmaximo = form.cleaned_data['stockmaximo']
            inventario.save()
        
        return response

class DetalleCompraUpdate(BSModalUpdateView):
    model = Detallecompra
    form_class = DetalleCompraForm
    template_name = 'compra/detallecompraedit.html'
    success_message = 'Hecho! Detalle Actualizado Correctamente.'
    
    def get_object(self, queryset=None):
        compra_id = self.kwargs.get('compra_id')
        pk = self.kwargs.get('pk')
        return get_object_or_404(Detallecompra, pk=pk, compra_id=compra_id)
    
    def get_success_url(self):
        return reverse('compra:compraread', kwargs={'pk': self.kwargs.get('compra_id')})

    def form_valid(self, form):
        detallecompra = self.get_object()

        # Verificar si la cantidad es 0
        cantidad = form.cleaned_data['cantidad']
        if cantidad == 0:
            messages.error(self.request, 'La cantidad del producto no puede ser 0.')
            return redirect('compra:compraread', pk=self.kwargs.get('compra_id'))

        # Obtener la diferencia entre la cantidad anterior y la cantidad actual
        cantidad_anterior = detallecompra.cantidad 
        diferencia_cantidad = cantidad - cantidad_anterior

        # Obtener el producto y la sucursal
        producto_id = form.cleaned_data['producto'].id
        sucursal_id = self.request.session.get('sucursal')

        # Actualizar el inventario
        try:
            inventario = Inventario.objects.get(producto_id=producto_id, sucursal_id=sucursal_id)
            inventario.stock += diferencia_cantidad
            inventario.save()
        except Inventario.DoesNotExist:
            pass  # Manejar la excepción si no existe el registro en inventario

        return super().form_valid(form)

class DetalleCompraDelete(BSModalDeleteView):
    model = Detallecompra
    template_name = 'compra/detallecompradelete.html'
    success_message = 'Hecho! Compra Eliminada Correctamente.'
    
    def get_success_url(self):
        return reverse('compra:compraread', kwargs={'pk': self.kwargs.get('compra_id')})
    
    def form_valid(self, form):
        detallecompra = self.get_object()
        
        if detallecompra is None:
            # Manejar el caso en el que el objeto no se encuentra
            print("Objeto Detallecompra no encontrado")
        else:
            # Procesar el objeto detallecompra
            # print(f"ID de Detallecompra: {detallecompra.id}")

            # Obtener la cantidad a eliminar del inventario
            cantidad = detallecompra.cantidad

            # Obtener el producto y la sucursal
            producto_id = detallecompra.producto.id
            sucursal_id = self.request.session.get('sucursal')

            # Actualizar el inventario
            try:
                inventario = Inventario.objects.get(producto_id=producto_id, sucursal_id=sucursal_id)
                inventario.stock -= cantidad
                inventario.save()
                #if inventario.stock ==0:
                #    inventario.delete()
                    
            except Inventario.DoesNotExist:
                inventario = Inventario(producto_id=producto_id, sucursal_id=sucursal_id, stock=0)
                inventario.save()

            # Eliminar el detalle de compra
            detallecompra.delete()

            return super().form_valid(form)
   
############################################################################################    
    
def Sessiones(request):
    # Obtener todas las claves y valores de la sesión
    session_data = request.session.items()
    
    # Pasar los datos de sesión al contexto
    context = {
        'session_data': session_data
    }
    
    return render(request, 'compra/sessiones.html', context)

############################################################################################

def verificar_inventario(request):
    if request.method == 'GET' and 'producto_id' in request.GET:
        producto_id = request.GET.get('producto_id')
        # Verifica si el producto está en el inventario
        en_inventario = Inventario.objects.filter(producto_id=producto_id).exists()
        return JsonResponse({'en_inventario': en_inventario})
    else:
        return JsonResponse({'error': 'No se proporcionó el ID del producto o la solicitud no es de tipo GET'})
