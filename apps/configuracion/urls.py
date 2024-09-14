from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import EmpresaList, EmpresaCreate, EmpresaUpdate, EmpresaDelete, SucursaleList, \
    SucursaleCreate, SucursaleUpdate, SucursaleDelete , ConfiguracioneList, ConfiguracioneCreate, \
    ConfiguracioneUpdate, ConfiguracioneDelete, CorrelativoFactList, CorrelativoFactCreate, \
    CorrelativoFactUpdate, CorrelativoFactDelete

app_name = 'configuracion'


urlpatterns = [
    path('empresas/', login_required(EmpresaList.as_view()), name='empresalist'),
    path('empresas/create/', login_required(EmpresaCreate.as_view()), name='empresacreate'),
    path('empresas/edit/<int:pk>/', login_required(EmpresaUpdate.as_view()), name='empresaedit'),
    path('empresas/delete/<int:pk>/', login_required(EmpresaDelete.as_view()), name='empresadelete'),
    
    path('sucursales/', login_required(SucursaleList.as_view()), name='sucursallist'),
    path('sucursales/create/', login_required(SucursaleCreate.as_view()), name='sucursalcreate'),
    path('sucursales/edit/<int:pk>/', login_required(SucursaleUpdate.as_view()), name='sucursaledit'),
    path('sucursales/delete/<int:pk>/', login_required(SucursaleDelete.as_view()), name='sucursaldelete'),
    
    path('configuraciones/', login_required(ConfiguracioneList.as_view()), name='configuracionlist'),
    path('configuraciones/create/', login_required(ConfiguracioneCreate.as_view()), name='configuracioncreate'),
    path('configuraciones/edit/<int:pk>/', login_required(ConfiguracioneUpdate.as_view()), name='configuracionedit'),
    path('configuraciones/delete/<int:pk>/', login_required(ConfiguracioneDelete.as_view()), name='configuraciondelete'),
    
    path('correlativos/', login_required(CorrelativoFactList.as_view()), name='correlativolist'),
    path('correlativos/create/', login_required(CorrelativoFactCreate.as_view()), name='correlativocreate'),
    path('correlativos/edit/<int:pk>/', login_required(CorrelativoFactUpdate.as_view()), name='correlativoedit'),
    path('correlativos/delete/<int:pk>/', login_required(CorrelativoFactDelete.as_view()), name='correlativodelete'),

]
