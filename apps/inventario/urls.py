from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete, ProductoList, \
    ProductoCreate, ProductoUpdate, ProductoDelete , EspecialeList, EspecialeCreate, \
    EspecialeUpdate, EspecialeDelete, InventarioList, InventarioCreate, \
    InventarioUpdate, InventarioDelete, procesar_csv

app_name = 'inventario'

urlpatterns = [
    path('procesar-csv/', procesar_csv, name='procesar_csv'),
    
    path('categorias/', login_required(CategoriaList.as_view()), name='categorialist'),
    path('categorias/create/', login_required(CategoriaCreate.as_view()), name='categoriacreate'),
    path('categorias/edit/<int:pk>/', login_required(CategoriaUpdate.as_view()), name='categoriaedit'),
    path('categorias/delete/<int:pk>/', login_required(CategoriaDelete.as_view()), name='categoriadelete'),
    
    path('productos/', login_required(ProductoList.as_view()), name='productolist'),
    path('productos/create/', login_required(ProductoCreate.as_view()), name='productocreate'),
    path('productos/edit/<int:pk>/', login_required(ProductoUpdate.as_view()), name='productoedit'),
    path('productos/delete/<int:pk>/', login_required(ProductoDelete.as_view()), name='productodelete'),
    
    path('especiales/', login_required(EspecialeList.as_view()), name='especialelist'),
    path('especiales/create/', login_required(EspecialeCreate.as_view()), name='especialecreate'),
    path('especiales/edit/<int:pk>/', login_required(EspecialeUpdate.as_view()), name='especialeedit'),
    path('especiales/delete/<int:pk>/', login_required(EspecialeDelete.as_view()), name='especialedelete'),
    
    path('inventarios/', login_required(InventarioList.as_view()), name='inventariolist'),
    path('inventarios/create/', login_required(InventarioCreate.as_view()), name='inventariocreate'),
    path('inventarios/edit/<int:pk>/', login_required(InventarioUpdate.as_view()), name='inventarioedit'),
    path('inventarios/delete/<int:pk>/', login_required(InventarioDelete.as_view()), name='inventariodelete'),
	
 
]
