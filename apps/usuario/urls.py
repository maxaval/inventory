from django.urls import include, path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import index, UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete, dashboard, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/usuario/login'), name='logout'),
	path('', index, name = 'index'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('list/', login_required(UsuarioList.as_view()), name= 'usuariolist'),
	path('add/', login_required(UsuarioCreate.as_view()), name = 'usuarioadd'),
	path('edit/<int:pk>/', login_required(UsuarioUpdate.as_view()), name= 'usuarioedit'),
	path('delete/<int:pk>/', login_required(UsuarioDelete.as_view()), name = 'usuariodelete'),
]