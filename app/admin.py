from django.contrib import admin
from app.models import *
# Register your models here.
# aqui podemos cadastrar dados no banco usando o /admin

from django.contrib import admin
from app.models import Barbeiro

class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ('idBarbeiro', 'NomeBarbeiro',
                    'telefoneBarbeiro', 'fotoBarbeiro')
    
    search_fields = ('idBarbeiro', 'NomeBarbeiro',
                    'telefoneBarbeiro')
    
    list_per_page = 100

admin.site.register(Barbeiro, BarbeiroAdmin)

