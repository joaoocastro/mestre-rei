from django import forms
from django.core.exceptions import ValidationError
from app.models import Agendamento, Barbeiro, Cliente, Barbearia, Agenda, Trabalha
import datetime

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('barbearia', 'barbeiro', 'data', 'horario')

        widgets = {
            'barbearia': forms.Select(attrs={'class': 'form-control'}),
            'barbeiro': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_data(self):
        """
        Validação do campo 'data': não pode ser no passado.
        """
        data = self.cleaned_data.get('data')

        if not data:
            raise ValidationError('O campo data é obrigatório.')

        # Validação: data no passado
        if data < datetime.date.today():
            raise ValidationError('Data inválida - agendamento no passado.')

        return data

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('agenda', 'cliente')

        widgets = {
            'agenda': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class TrabalhaForm(forms.ModelForm):
    class Meta:
        model = Trabalha
        fields = '__all__'
