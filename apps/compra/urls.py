from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import verificar_inventario, CompraList, CompraCreate, CompraUpdate, CompraDelete, CompraRead, DetalleCompraCreate, DetalleCompraDelete, DetalleCompraList, DetalleCompraUpdate, ProveedoreList, ProveedoreCreate, ProveedoreUpdate, ProveedoreDelete, Sessiones

app_name = 'compra'

urlpatterns = [
    
    path('proveedores/', login_required(ProveedoreList.as_view()), name='proveedorelist'),
    path('proveedores/create/', login_required(ProveedoreCreate.as_view()), name='proveedorecreate'),
    path('proveedores/edit/<int:pk>/', login_required(ProveedoreUpdate.as_view()), name='proveedoreedit'),
    path('proveedores/delete/<int:pk>/', login_required(ProveedoreDelete.as_view()), name='proveedoredelete'),
    
    path('compras/sesiones', Sessiones, name = 'sesiones'),
    path('compras/', login_required(CompraList.as_view()), name='compralist'),
    path('compras/create/', login_required(CompraCreate.as_view()), name='compracreate'),
    path('compras/read/<int:pk>/', login_required(CompraRead.as_view()), name='compraread'),
    path('compras/edit/<int:pk>/', login_required(CompraUpdate.as_view()), name='compraedit'),
    path('compras/delete/<int:pk>/', login_required(CompraDelete.as_view()), name='compradelete'),
    
    path('detallecompras/', login_required(DetalleCompraList.as_view()), name='detallecompralist'),
    path('detallecompras/create/<int:compra_id>/', login_required(DetalleCompraCreate.as_view()), name='detallecompracreate'),
    path('detallecompras/edit/<int:pk>/<int:compra_id>/', login_required(DetalleCompraUpdate.as_view()), name='detallecompraedit'),
    path('detallecompras/delete/<int:pk>/<int:compra_id>/', login_required(DetalleCompraDelete.as_view()), name='detallecompradelete'),
    path('detallecompras/verificar-inventario/', verificar_inventario, name='verificar_inventario'),
]