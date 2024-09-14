# forms.py
from django import forms
from django.apps import apps
from .models import Categoria, Producto, Especiale, Inventario
from bootstrap_modal_forms.forms import BSModalModelForm

class CategoriaForm(BSModalModelForm):
    class Meta:
        model = Categoria
        fields = [
			'nombre',
			'descripcion',
		]
        labels = {
   
			'nombre' : 'Nombre de Categoría',
			'descripcion' : 'Descripción Categoría',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Categoría'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Descripcion Categoría'}),
        }
        
class ProductoForm(BSModalModelForm):
    class Meta:
        model = Producto
        fields = [
            'categoria',
			'codigo',
			'nombre',
            'descripcion',
            'photo',
            'contenedor',
            'cantidadcontenedor',
            
		]
        labels = {
            'categoria' : 'Nombre Categoría',
			'codigo' : 'Codigo Producto',
			'nombre' : 'Nombre Producto',
            'descripcion' : 'Descripción Producto',
            'photo' : 'Foto Producto',
            'contenedor' : 'Contenedor Producto',
            'cantidadcontenedor' : 'Cantidad Contenedor',
        }
        widgets = {
            'categoria': forms.ModelChoiceField(queryset=Categoria.objects.all()),
			'codigo' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Codigo Producto'}),
			'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Producto'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Descripción Producto'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder': 'Seleccione Imagen Producto'}),
            'contenedor' : forms.Select(attrs={'class':'form-control'}),
            'cantidadcontenedor' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Cantidad Contenedor'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar las opciones del campo 'categoria' solo para las categorías de productos
        self.fields['categoria'].queryset = Categoria.objects.filter(producto__isnull=False).distinct()
        
class EspecialeForm(BSModalModelForm):
    class Meta:
        model = Especiale
        fields = [
			'producto',
			'cantidad',
            'precio',
		]
        labels = {
            'producto' : 'Nombre de Producto',
			'cantidad' : 'Cantidad Producto',
            'precio' : 'Precio Producto',
        }
        widgets = {
            'producto': forms.Select(attrs={'class':'form-control','placeholder': 'Nombre Categoría'}),
			'cantidad': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Categoría'}),
            'precio': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Categoría'}),
        }
        
class InventarioForm(BSModalModelForm):
    class Meta:
        model = Inventario
        fields = [
            'sucursal',
			'producto',
			'stock',
            'stockminimo',
            'stockmaximo',
            'preciocompra',
            'utilidad',
            'iva',
            'precioventa',
		]
        labels = {
            'sucursal' : 'Nombre Sucursal',
			'producto' : 'Nombre Producto',
			'stock' : 'Stock',
            'stockminimo' : 'Stock Minimo',
            'stockmaximo' : 'Stock Maximo',
            'preciocompra' : 'Precio Compra',
            'utilidad' : 'Utilidad',
            'iva' : 'IVA',
            'precioventa' : 'Precio Venta',
        }
        widgets = {
            'sucursal' : forms.Select(attrs={'class':'form-control'}),
			'producto' : forms.Select(attrs={'class':'form-control'}),
			'stock' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Stock Producto'}),
            'stockminimo' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Stock Minimo Producto'}),
            'stockmaximo' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Stock Maximo Producto'}),
            'preciocompra' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Precio Compra'}),
            'utilidad' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Utilidad'}),
            'iva' : forms.TextInput(attrs={'class':'form-control','placeholder': 'IVA'}),
            'precioventa' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Precio Venta'}),
        }
        
class CsvProcessorForm(forms.Form):
    modelos_inventario = [(model.__name__, model.__name__) for model in apps.get_app_config('inventario').get_models()]
    modelo = forms.ChoiceField(choices=modelos_inventario, label='Selecciona el modelo')
    archivo = forms.FileField(label='Selecciona el Archivo CSV')
    progreso = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        