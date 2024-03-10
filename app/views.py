from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Barbeiro, Barbearia, Cliente, Trabalha, Agendamento

# Views para o modelo Barbeiro
class BarbeiroListView(ListView):
    model = Barbeiro
    template_name = 'barbeiro_list.html'  # Substitua pelo nome do seu template
    context_object_name = 'barbeiros'

class BarbeiroDetailView(DetailView):
    model = Barbeiro
    template_name = 'barbeiro_detail.html'  # Substitua pelo nome do seu template
    context_object_name = 'barbeiro'

class BarbeiroCreateView(CreateView):
    model = Barbeiro
    template_name = 'barbeiro_form.html'  # Substitua pelo nome do seu template
    fields = '__all__'

class BarbeiroUpdateView(UpdateView):
    model = Barbeiro
    template_name = 'barbeiro_form.html'  # Substitua pelo nome do seu template
    fields = '__all__'

class BarbeiroDeleteView(DeleteView):
    model = Barbeiro
    template_name = 'barbeiro_confirm_delete.html'  # Substitua pelo nome do seu template
    success_url = reverse_lazy('barbeiro-list')  # Substitua pelo nome da sua URL de listagem de barbeiros

# Views para o modelo Barbearia
class BarbeariaListView(ListView):
    model = Barbearia
    template_name = 'barbearia_list.html'
    context_object_name = 'barbearias'

class BarbeariaDetailView(DetailView):
    model = Barbearia
    template_name = 'barbearia_detail.html'
    context_object_name = 'barbearia'

class BarbeariaCreateView(CreateView):
    model = Barbearia
    template_name = 'barbearia_form.html'
    fields = '__all__'

class BarbeariaUpdateView(UpdateView):
    model = Barbearia
    template_name = 'barbearia_form.html'
    fields = '__all__'

class BarbeariaDeleteView(DeleteView):
    model = Barbearia
    template_name = 'barbearia_confirm_delete.html'
    success_url = reverse_lazy('barbearia-list')

# Views para o modelo Cliente (repita o padrão semelhante ao modelo Barbeiro)
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

# Views para o modelo Trabalha (repita o padrão semelhante ao modelo Barbeiro)
class TrabalhaListView(ListView):
    model = Trabalha
    template_name = 'trabalha_list.html'
    context_object_name = 'trabalhas'

class TrabalhaDetailView(DetailView):
    model = Trabalha
    template_name = 'trabalha_detail.html'
    context_object_name = 'trabalha'

class TrabalhaCreateView(CreateView):
    model = Trabalha
    template_name = 'trabalha_form.html'
    fields = '__all__'

class TrabalhaUpdateView(UpdateView):
    model = Trabalha
    template_name = 'trabalha_form.html'
    fields = '__all__'

class TrabalhaDeleteView(DeleteView):
    model = Trabalha
    template_name = 'trabalha_confirm_delete.html'
    success_url = reverse_lazy('trabalha-list')

# Views para o modelo Agendamento (repita o padrão semelhante ao modelo Barbeiro)
class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'agendamento_list.html'
    context_object_name = 'agendamentos'

class AgendamentoDetailView(DetailView):
    model = Agendamento
    template_name = 'agendamento_detail.html'
    context_object_name = 'agendamento'

class AgendamentoCreateView(CreateView):
    model = Agendamento
    template_name = 'agendamento_form.html'
    fields = '__all__'

class AgendamentoUpdateView(UpdateView):
    model = Agendamento
    template_name = 'agendamento_form.html'
    fields = '__all__'

class AgendamentoDeleteView(DeleteView):
    model = Agendamento
    template_name = 'agendamento_confirm_delete.html'
    success_url = reverse_lazy('agendamento-list')
