from django import forms
from .models import Proveedore, Compra, Detallecompra
from apps.inventario.models import Inventario
from bootstrap_modal_forms.forms import BSModalModelForm

class ProveedoreForm(BSModalModelForm):
    class Meta:
        model = Proveedore
        fields = [
            'nombre',
			'representante',
			'direccion',
			'nit',
            'iva',
            'tel',
            'email',
            'descripcion',			
		]
        labels = {   
            'nombre' : 'Nombre Empresa',
			'representante' : 'Nombre Representante',
			'direccion' : 'Dirección',
			'nit' : 'NIT Empresa',
            'iva' : 'IVA Empresa',
            'tel' : 'Telefono Empresa',
            'email' : 'Email',
            'descripcion' : 'Descripcion Proveedor',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Empresa'}),
            'representante': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Representante'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Dirección'}),
            'nit': forms.TextInput(attrs={'class':'form-control','placeholder': 'NIT Empresa'}),
            'iva': forms.TextInput(attrs={'class':'form-control','placeholder': 'IVA Empresa'}),
            'tel': forms.TextInput(attrs={'class':'form-control','placeholder': 'Telefono Empresa'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Descripcion Proveedor'}),
        }
        
class CompraForm(BSModalModelForm):
    class Meta:
        model = Compra
        fields = [
            'proveedor',
			'factura',
			'descripcion',
			'pagocaja',
            'estado',
            'bonificacion',
            'totalcompra',		
		]
        labels = {   
            'proveedor' : 'Proveedor',
			'factura' : 'No. Factura',
			'descripcion' : 'Descripción',
			'pagocaja' : 'Pago de Caja',
            'estado' : 'Estado Factura',
            'bonificacion' : 'Bonificación',
            'totalcompra' : 'Total Compra',        }
        widgets = {
            'proveedor' : forms.Select(attrs={'class':'form-control','placeholder': 'Proveedor'}),
            'factura': forms.TextInput(attrs={'class':'form-control','placeholder': 'No. Factura'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Descripción'}),
            'pagocaja': forms.CheckboxInput(attrs={'class':'form-control','placeholder': 'Pago de Caja'}),
            'estado': forms.Select(attrs={'class':'form-control','placeholder': 'Estado Factura'}),
            'bonificacion': forms.CheckboxInput(attrs={'class':'form-control','placeholder': 'Bonificación'}),
            'totalcompra': forms.TextInput(attrs={'class':'form-control','placeholder': 'Total Compra'}),
        }
        
class DetalleCompraForm(BSModalModelForm):
    stockminimo = forms.IntegerField(label='Stock Mínimo', required=False)
    stockmaximo = forms.IntegerField(label='Stock Máximo', required=False)
    precioventa = forms.DecimalField(label='Precio Venta', required=False, decimal_places=2) 
    
    class Meta:
        model = Detallecompra
        fields = [
            'producto',
			'cantidad',
			'preciounitario',
			'preciototal',
		]
        labels = {   
            'producto' : 'Producto',
			'cantidad' : 'Cantidad',
			'preciounitario' : 'Precio Unitario',
			'preciototal' : 'Precio Total',
        }
        widgets = {
            'producto' : forms.Select(attrs={'class':'form-control required=True'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control','placeholder': 'Cantidad'}),
            'preciounitario': forms.TextInput(attrs={'class':'form-control','placeholder': 'Precio Unitario'}),
            'preciototal': forms.TextInput(attrs={'class':'form-control','placeholder': 'Precio Total'}),
            'compra': forms.HiddenInput(),
        }
