"""
Configuração de URL para o projeto admin.

A lista `urlpatterns` roteia URLs para views. Para mais informações, veja:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemplos:
Views baseadas em função
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL a urlpatterns:  path('', views.home, name='home')
Views baseadas em classe
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outra URLconf
    1. Importe a função include: from django.urls import include, path
    2. Adicione uma URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import (
    HomeView, CustomLoginView, SignUpView, RenderTemplateView,
    BarbeiroListView, BarbeiroDetailView, BarbeiroCreateView,
    BarbeiroUpdateView, BarbeiroDeleteView, ClienteListView,
    ClienteDetailView, ClienteCreateView, ClienteUpdateView,
    ClienteDeleteView, BarbeariaListView, BarbeariaDetailView,
    BarbeariaCreateView, BarbeariaUpdateView, BarbeariaDeleteView,
    TrabalhaListView, TrabalhaDetailView, TrabalhaCreateView,
    TrabalhaUpdateView, TrabalhaDeleteView, AgendaListView, AgendaCreateView, AgendaDetailView,
    AgendamentoListView, AgendamentoCreateView, AgendaDeleteView, AgendaUpdateView,
)
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # administrador
    path('', HomeView.as_view(), name='home'),  # home
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

    # Agenda
    path('agendas/', AgendaListView.as_view(), name='agenda-list'),
    path('agendas/add/', AgendaCreateView.as_view(), name='agenda-add'),
    path('agendas/<int:pk>/', AgendaDetailView.as_view(), name='agenda-detail'),
    path('agendas/<int:pk>/update/', AgendaUpdateView.as_view(), name='agenda-update'),
    path('agendas/<int:pk>/delete/', AgendaDeleteView.as_view(), name='agenda-delete'),

    # Agendamento
    path('agendamentos/', AgendamentoListView.as_view(), name='agendamento-list'),
    path('agendamentos/add/', AgendamentoCreateView.as_view(), name='agendamento-add'),
    # path('agendamentos/add/', AgendamentoDetailView.as_view(), name='agendamento-detail'),
    # path('agendamentos/add/', AgendamentoUpdateView.as_view(), name='agendamento-update'),
    # path('agendamentos/add/', AgendamentoDeleteView.as_view(), name='agendamento-delete'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)