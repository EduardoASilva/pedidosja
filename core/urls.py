"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from pedidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout'),
    path('enviar_pedidos/', views.enviar_pedido, name='enviar_pedido'),
    path('comandas/', views.comandas, name='comandas'),
    path('finalizar_pedido/<int:id_pedido>', views.finalizar_pedido, name='finalizar_pedido'),
    path('relatorio/', views.relatorio, name='relatorio'),
]
