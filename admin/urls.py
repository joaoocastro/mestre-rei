"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import * # importar todas as views para uso aqui nas urls
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls), #administrador
    path('', HomeView.as_view(), name='home'), # home
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('render_template/<str:template_name>/', RenderTemplateView.as_view(), name='render_template'),
    
    path('barbeiros/', BarbeiroListView.as_view(), name='barbeiro-list'),
    path('barbeiros/<int:pk>/', BarbeiroDetailView.as_view(), name='barbeiro-detail'),
    path('barbeiros/add/', BarbeiroCreateView.as_view(), name='barbeiro-add'),
    path('barbeiros/<int:pk>/update/', BarbeiroUpdateView.as_view(), name='barbeiro-update'),
    path('barbeiros/<int:pk>/delete/', BarbeiroDeleteView.as_view(), name='barbeiro-delete'),

    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),  # Detalhes de um cliente
    path('clientes/add/', ClienteCreateView.as_view(), name='cliente-add'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='cliente-update'),  # Atualizar um cliente existente
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),  # Deletar um cliente existente
    
    path('barbearias/', BarbeariaListView.as_view(), name='barbearia-list'),  # Listar barbearias
    path('barbearias/<int:pk>/', BarbeariaDetailView.as_view(), name='barbearia-detail'),  # Detalhes da barbearia
    path('barbearias/add/', BarbeariaCreateView.as_view(), name='barbearia-add'),  # Adicionar nova barbearia
    path('barbearias/<int:pk>/update/', BarbeariaUpdateView.as_view(), name='barbearia-update'),  # Atualizar barbearia
    path('barbearias/<int:pk>/delete/', BarbeariaDeleteView.as_view(), name='barbearia-delete'),  # Deletar barbearia
    
    path('trabalhos/', TrabalhaListView.as_view(), name='trabalha-list'),  # Listar 'trabalhas'
    path('trabalhos/<int:pk>/', TrabalhaDetailView.as_view(), name='trabalha-detail'),  # Detalhes de um 'trabalha'
    path('trabalhos/add/', TrabalhaCreateView.as_view(), name='trabalha-add'),  # Adicionar novo 'trabalha'
    path('trabalhos/<int:pk>/update/', TrabalhaUpdateView.as_view(), name='trabalha-update'),  # Atualizar 'trabalha'
    path('trabalhos/<int:pk>/delete/', TrabalhaDeleteView.as_view(), name='trabalha-delete'),  # Deletar 'trabalha'

]

