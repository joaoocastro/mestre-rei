from django.contrib import admin
from app.models import *
# Register your models here.
# aqui podemos cadastrar dados no banco usando o /admin

from django.contrib import admin
from app.models import Barbeiro
from app.models import Cliente
from app.models import Barbearia

class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ('idBarbeiro', 'NomeBarbeiro',
                    'telefoneBarbeiro', 'fotoBarbeiro')
    
    search_fields = ('idBarbeiro', 'NomeBarbeiro',
                    'telefoneBarbeiro')
    
    list_per_page = 100

admin.site.register(Barbeiro, BarbeiroAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('idCliente', 'NomeCliente',
                    'telefoneCliente', 'fotoCliente')
    
    search_fields = ('idCliente', 'NomeCliente',
                    'telefoneCliente')
    
    list_per_page = 100

admin.site.register(Cliente)

class BarbeariaAdmin(admin.ModelAdmin):
    list_display = ('idBarbearia', 'nome',
                    'endereco', ' hrAbertura',' hrFechamento')
    
    search_fields = ('idBarbearia', 'nome',
                    'endereco', ' hrAbertura',' hrFechamento')
    
    list_per_page = 100

admin.site.register(Barbearia)

