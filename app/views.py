from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Agenda, Barbeiro, Barbearia, Cliente, Trabalha, Agendamento
from .forms import AgendamentoForm, AgendaForm, TrabalhaForm

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Agenda
from .forms import AgendaForm
from django.contrib.messages.views import SuccessMessageMixin


class RenderTemplateView(View):
    def get(self, request, template_name):
        # Renderiza o template
        html = render_to_string(template_name + '.html', context={}, request=request)
        return HttpResponse(html)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'login.html'


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbeiros'] = Barbeiro.objects.all()
        context['barbearias'] = Barbearia.objects.all()
        context['clientes'] = Cliente.objects.all()
        context['trabalhos'] = Trabalha.objects.all()
        context['agendamentos'] = Agendamento.objects.all()
        context['agendas'] = Agenda.objects.all()
        return context


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
    template_name = 'barbeiro_form.html'
    fields = '__all__'
    success_url = reverse_lazy('barbeiro-add')  # Redireciona para a mesma página para cadastrar outro barbeiro

    def form_valid(self, form):
        messages.success(self.request, 'Barbeiro cadastrado com sucesso!')
        return super().form_valid(form)

class BarbeiroUpdateView(UpdateView):
    model = Barbeiro
    template_name = 'barbeiro_form.html'  # Substitua pelo nome do seu template
    fields = '__all__'
    success_url = reverse_lazy('barbeiro-list')

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
    success_url = reverse_lazy('barbearia-add')
    
    def form_valid(self, form):
        messages.success(self.request, 'Barbearia cadastrada com sucesso!')
        return super().form_valid(form)

class BarbeariaUpdateView(UpdateView):
    model = Barbearia
    template_name = 'barbearia_form.html'
    fields = '__all__'
    success_url = reverse_lazy('barbearia-list')

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
    success_url = reverse_lazy('cliente-add')  # Redireciona para a mesma página para cadastrar outro cliente

    def form_valid(self, form):
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
        return super().form_valid(form)


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

# Views para o modelo Trabalha (repita o padrão semelhante ao modelo Barbeiro)
class TrabalhaListView(ListView):
    model = Trabalha
    template_name = 'trabalha_list.html'
    context_object_name = 'trabalhos'

class TrabalhaDetailView(DetailView):
    model = Trabalha
    template_name = 'trabalha_detail.html'
    context_object_name = 'trabalha'

class TrabalhaCreateView(CreateView):
    model = Trabalha
    template_name = 'trabalha_form.html'
    fields = '__all__'
    success_url = reverse_lazy('trabalha-add')
    
    # permite mostrar lista com barbeiros e barbearias no front
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbeiros'] = Barbeiro.objects.all()
        context['barbearias'] = Barbearia.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Trabalho cadastrado com sucesso!')
        return super().form_valid(form)
    
class TrabalhaUpdateView(UpdateView):
    model = Trabalha
    template_name = 'trabalha_form.html'
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbeiros'] = Barbeiro.objects.all()
        context['barbearias'] = Barbearia.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Trabalho cadastrado com sucesso!')
        return super().form_valid(form)

class TrabalhaDeleteView(DeleteView):
    model = Trabalha
    template_name = 'trabalha_confirm_delete.html'
    success_url = reverse_lazy('trabalha-list')


# Views para o modelo Agendamento (repita o padrão semelhante ao modelo Barbeiro)
def listar_agenda(request):
    agendas = Agenda.objects.all()
    return render(request, 'listar_agenda.html', {'agendas': agendas})

def cadastrar_agenda(request):
    if request.method == "POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agenda')
    else:
        form = AgendaForm()
    return render(request, 'cadastrar_agenda.html', {'form': form})

def cadastrar_agendamento(request):
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')
    else:
        form = AgendamentoForm()
    return render(request, 'cadastrar_agendamento.html', {'form': form})


# Listar Agendas
class AgendaListView(ListView):
    model = Agenda
    template_name = 'agenda_list.html'
    context_object_name = 'agendas'

# Cadastrar Agenda
class AgendaCreateView(SuccessMessageMixin, CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agenda-list')
    success_message = "Agenda cadastrada com sucesso!"


# Listar Agendamentos
class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'agendamento_list.html'
    context_object_name = 'agendamentos'

# Cadastrar Agendamento
class AgendamentoCreateView(SuccessMessageMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamento-list')
    success_message = "Agendamento cadastrado com sucesso!"
