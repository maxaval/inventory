"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout', logout_then_login, name = 'logout'),
    path('configuracion/', include('apps.configuracion.urls', namespace = 'configuracion')),
    path('inventario/', include('apps.inventario.urls', namespace = 'inventario')),
    path('compra/', include('apps.compra.urls', namespace = 'compra')),
    path('venta/', include('apps.venta.urls', namespace = 'venta')),
    path('usuario/', include('apps.usuario.urls', namespace = 'usuario')),
]
