from django import forms
from django.forms import fields, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import UserProfile
from bootstrap_modal_forms.forms import BSModalModelForm
from django.contrib.auth.forms import AuthenticationForm
from apps.configuracion.models import Sucursale


class CustomAuthenticationForm(AuthenticationForm):
    sucursal = forms.ModelChoiceField(queryset=Sucursale.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['sucursal'].widget.attrs.update({'class': 'form-control'})


class RegistroForm(UserCreationForm, BSModalModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
			'username',
			'first_name',
			'last_name',
			'password1',
			'password2',
			'email',
			'is_active',
			'is_superuser',
   			'is_staff',
			'dui',
			'nit',
			'nomafp',
			'numafp',
			'isss',
			'antecedente',
			'solvencia',
			'vacunaCOVID',
   			'nombrebanco',
			'cuentabanco',
			'instituciondisc',
			'discapacidad',
			'direccion',
			'telefono',
			'celular',
			'nomemergencia',
			'parenemergencia',
			'telemergencia',
			'estudios',
			'curriculum',
			'cargo',
			'sexo',
			'fecha_in',
			'fecha_exp',
			'foto',
			'salario',
			'viaticos',
			'cafeteria',
			'comision',
			'wallet',
			'sucursal',
		]
        labels = {
   
			'username' : 'Nombre de Usuario',
			'first_name' : 'Nombres',
			'last_name' : 'Apellidos',
			'password1' : 'Contraseña',
			'password2' : 'Repita Contraseña',
			'email' : 'Email',
			'is_active' : 'Activo',
			'is_superuser' : 'Super Usuario',
   			'is_staff' : 'Staff',
			'dui' : 'DUI',
			'nit' : 'NIT',
			'nomafp' : 'Nombre AFP',
			'numafp' : 'Numero AFP',
			'isss' : 'ISSS',
			'antecedente' : 'Antecedentes',
			'solvencia' : 'Solvencia',
			'vacunaCOVID' : 'COVID',
			'nombrebanco' : 'Nombre Banco',
			'cuentabanco' : 'Numero de Cuenta',
			'instituciondisc' : 'Institución Discapacitado',
			'discapacidad' : 'Discapacidad',
			'direccion' : 'Direccion',
			'telefono' : 'Telefono',
			'celular' : 'Celular',
			'nomemergencia' : 'Nombre Emergencia',
			'parenemergencia' : 'Parentezco Emergencia',
			'telemergencia' : 'Telefono Emergencia',
			'estudios' : 'Estudios',
			'curriculum' : 'Curriculum',
			'cargo' : 'Cargo',
			'sexo' : 'Sexo',
			'fecha_in' : 'Fecha Ingreso',
			'fecha_exp' : 'Fecha Despido',
			'foto' : 'Foto',
			'salario' : 'Salario',
			'viaticos' : 'Viaticos',
			'cafeteria' : 'Cafeteria',
			'comision' : 'Comision',
			'wallet' : 'Wallet',
			'sucursal' : 'Sucursal',
		}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': 'Usuario'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Apellidos'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}),
			'is_active' : forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
			'is_superuser' : forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
   			'is_staff' : forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'dui': forms.TextInput(attrs={'class':'form-control','placeholder': 'DUI'}),
            'nit': forms.TextInput(attrs={'class':'form-control','placeholder': 'NIT'}),
            'nomafp': forms.Select(attrs={'class':'form-control','placeholder': 'Nombre AFP'}),
            'numafp': forms.TextInput(attrs={'class':'form-control','placeholder': 'Numero AFP'}),
            'isss': forms.TextInput(attrs={'class':'form-control','placeholder': 'Numero ISSS'}),
            'antecedente': forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'solvencia': forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'vacunaCOVID': forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'nombrebanco' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Banco de Banco'}),
            'cuentabanco' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Cuenta de Banco'}),
            'instituciondisc': forms.TextInput(attrs={'class':'form-control','placeholder': 'Institución que Discapacita'}),
            'discapacidad': forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Direccion'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder': 'Telefono'}),
            'celular': forms.TextInput(attrs={'class':'form-control','placeholder': 'Celular'}),
            'nomemergencia': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre a llamar en Emergencia'}),
            'parenemergencia': forms.Select(attrs={'class':'form-control','placeholder': 'Parentezco'}),
            'telemergencia': forms.TextInput(attrs={'class':'form-control','placeholder': 'Numero en caso de Emergencia'}),
            'estudios': forms.Select(attrs={'class':'form-control','placeholder': 'Estudios Realizados'}),
            'curriculum': forms.FileInput(attrs={'class':'form-control','placeholder': 'Curriculum'}),
            'cargo': forms.TextInput(attrs={'class':'form-control','placeholder': 'Cargo'}),
            'sexo': forms.TextInput(attrs={'class':'form-control','placeholder': 'Sexo'}),
            'fecha_in': forms.TextInput(attrs={'class':'form-control datetimepicker-input', 'data-target':"#fechaentrada",'placeholder': 'Fecha Ingreso'}),
            'fecha_exp': forms.TextInput(attrs={'class':'form-control datetimepicker-input', 'data-target':"#fechaexp",'placeholder': 'Fecha Expiración'}),
            'foto': forms.FileInput(attrs={'class':'custom-file-input', 'id':'foto', 'name': 'foto','placeholder': 'Seleccione el archivo'}),
            'salario': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Salario'}),
            'viaticos': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Viaticos'}),
            'cafeteria': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Cafetería'}),
            'comision': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Comisión'}),
            'wallet': forms.CheckboxInput(attrs={'data-toggle':'toggle', 'data-onstyle':'success', 'data-offstyle':'danger'}),
            'sucursal': forms.Select(attrs={'class':'form-control','placeholder': 'Sucursal'}),
        }
  