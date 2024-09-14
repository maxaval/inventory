from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.usuario.models import UserProfile
from apps.usuario.forms import RegistroForm, CustomAuthenticationForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'usuario/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        # Guarda la sucursal seleccionada en la sesión del usuario
        self.request.session['sucursal'] = form.cleaned_data['sucursal'].id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('usuario:index')  # Cambia esto a la URL deseada después del inicio de sesión


def index(request):
	return render(request, 'usuario/index.html')

def dashboard(request):
	return render(request, 'usuario/dashboard.html')

class UsuarioList(ListView):
	model = UserProfile
	template_name = 'usuario/usuariolist.html'

class UsuarioCreate(BSModalCreateView):
    model = UserProfile
    form_class = RegistroForm    
    template_name = "usuario/usuarioadd.html"
    success_message = 'Hecho! Usuario Creado Correctamente.'
    success_url = reverse_lazy('usuario:usuariolist')

class UsuarioUpdate(BSModalUpdateView):
    model = UserProfile
    form_class = RegistroForm
    template_name = 'usuario/usuarioedit.html'
    success_message = 'Hecho! Usuario Actualizado Correctamente.'
    success_url = reverse_lazy('usuario:usuariolist')
    
    def form_valid(self, form):
        # Obtén el usuario existente
        user = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        
        # Actualiza los campos del usuario con los datos del formulario
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.password1= form.cleaned_data['password1']
        user.password2= form.cleaned_data['password2']
        user.email = form.cleaned_data['email']
        user.is_active = form.cleaned_data['is_active']
        user.is_superuser = form.cleaned_data['is_superuser']
        user.is_staff = form.cleaned_data['is_staff']
        user.dui = form.cleaned_data['dui']
        user.nit = form.cleaned_data['nit']
        user.nomafp = form.cleaned_data['nomafp']
        user.numafp = form.cleaned_data['numafp']
        user.isss = form.cleaned_data['isss']
        user.antecedente = form.cleaned_data['antecedente']
        user.solvencia = form.cleaned_data['solvencia']
        user.vacunaCOVID = form.cleaned_data['vacunaCOVID']
        user.nombrebanco = form.cleaned_data['nombrebanco']
        user.cuentabanco = form.cleaned_data['cuentabanco']
        user.instituciondisc = form.cleaned_data['instituciondisc']
        user.discapacidad = form.cleaned_data['discapacidad']
        user.direccion = form.cleaned_data['direccion']
        user.telefono = form.cleaned_data['telefono']
        user.celular = form.cleaned_data['celular']
        user.nomemergencia = form.cleaned_data['nomemergencia']
        user.parenemergencia = form.cleaned_data['parenemergencia']
        user.telemergencia = form.cleaned_data['telemergencia']
        user.estudios = form.cleaned_data['estudios']
        user.curriculum = form.cleaned_data['curriculum']
        user.cargo = form.cleaned_data['cargo']
        user.sexo = form.cleaned_data['sexo']
        user.fecha_in = form.cleaned_data['fecha_in']
        user.fecha_exp = form.cleaned_data['fecha_exp']
        user.foto = form.cleaned_data['foto']
        user.salario = form.cleaned_data['salario']
        user.viaticos = form.cleaned_data['viaticos']
        user.cafeteria = form.cleaned_data['cafeteria']
        user.comision = form.cleaned_data['comision']
        user.wallet = form.cleaned_data['wallet']
        user.sucursal = form.cleaned_data['sucursal']
        
        # Guarda el usuario actualizado
        user.save()

        return super().form_valid(form)

class UsuarioDelete(BSModalDeleteView):
    model = UserProfile
    template_name = 'usuario/usuariodelete.html'
    success_message = 'Hecho! Usuario Eliminado Correctamente.'
    success_url = reverse_lazy('usuario:usuariolist')
