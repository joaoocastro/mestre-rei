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
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']

        # Check if the date is not in the past.
        if data < datetime.date.today():
            raise ValidationError('Data inválida - agendamento no passado.')

        # Check if the date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Data inválida - agendamento mais de 4 semanas à frente.')

        # Remember to always return the cleaned data.
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
