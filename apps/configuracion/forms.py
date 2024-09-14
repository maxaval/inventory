# forms.py
from django import forms
from .models import Empresa, Sucursale, Configuracione, CorrelativoFact
from bootstrap_modal_forms.forms import BSModalModelForm

class EmpresaForm(BSModalModelForm):
    class Meta:
        model = Empresa
        fields = [
			'nombre',
			'licencia',
			'fechaini',
			'fechafin',
			'logo',
			'about',
		]
        labels = {
   
			'nombre' : 'Nombre de Empresa',
			'licencia' : 'Licencia',
			'fechaini' : 'Fecha Inicio',
			'fechafin' : 'Fecha Fin',
			'logo' : 'Logo Empresa',
			'about' : 'Acerca Empresa',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Empresa'}),
            'licencia': forms.TextInput(attrs={'class':'form-control','placeholder': 'Licencia'}),
            'fechaini': forms.TextInput(attrs={'class':'form-control','placeholder': 'Fecha Inicio Licencia'}),
            'fechafin' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Fecha Fin Licencia'}),
            'logo' : forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder': 'Seleccione el Logo de su Empresa'}),
            'about' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Acerca Empresa'}),
        }
        

class SucursaleForm(BSModalModelForm):
    class Meta:
        model = Sucursale
        fields = [
            'empresa',
			'nombre',
			'direccion',
			'ipsucursal',			
		]
        labels = {   
            'empresa' : 'Empresa',
			'nombre' : 'Nombre de Sucursal',
			'direccion' : 'Dirección',
			'ipsucursal' : 'IP Sucursal',			
        }
        widgets = {
            'empresa' : forms.Select(attrs={'class':'form-control','placeholder': 'Empresa'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Sucursal'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Dirección'}),
            'ipsucursal': forms.TextInput(attrs={'class':'form-control','placeholder': 'IP Sucursal'}),
        }

class ConfiguracioneForm(BSModalModelForm):
    class Meta:
        model = Configuracione
        fields = [
			'sucursal',
			'utilidadactive',
			'utilidad',
			'ivaactive',
            'iva',
		]
        labels = {   
			'sucursal' : 'Nombre de Sucursal',
			'utilidadactive' : 'Activar Utilidad',
			'utilidad' : 'Porcentaje de Utilidad',
			'ivaactive' : 'Activar IVA',
            'iva' : 'Porcentaje IVA',
        }
        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control','placeholder': 'Nombre Sucursal'}),
            'utilidadactive': forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'utilidad': forms.TextInput(attrs={'class':'form-control','placeholder': 'Porcentaje Utilidad'}),
            'ivaactive' : forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'iva' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Porcentaje IVA'}),
        }

class CorrelativoFactForm(BSModalModelForm):
    class Meta:
        model = CorrelativoFact
        fields = [
			'sucursal',
			'tipodocumento',
			'correlativoini',
			'correlativofin',
			'numdocumentoasig',
			'fechadocumento',
            'correlativoact',
		]
        labels = {
   
			'sucursal' : 'Nombre de Sucursal',
			'tipodocumento' : 'Tipo Documento',
			'correlativoini' : 'Correlativo Inicio',
			'correlativofin' : 'Correlativo Fin',
			'numdocumentoasig' : 'Numero Docs Asignados',
			'fechadocumento' : 'Fecha Documento',
			'correlativoact' : 'Correlativo Actual',
        }
        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control','placeholder': 'Nombre Sucursal'}),
            'tipodocumento': forms.Select(attrs={'class':'form-control','placeholder': 'Tipo Documento'}),
            'correlativoini': forms.TextInput(attrs={'class':'form-control','placeholder': 'Inicio Correlativo'}),
            'correlativofin' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Fin Correlativo'}),
            'numdocumentoasig' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Numero Documento Asignación'}),
            'fechadocumento' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Fecha Documento Asignación'}),
            'correlativoact' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Correlativo Actual'}),
        }
