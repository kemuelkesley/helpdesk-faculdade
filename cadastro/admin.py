from django.contrib import admin

from cadastro.models import Condominio, Equipamento
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin


class EquipamentoInline(admin.StackedInline):  # Use admin.StackedInline para uma exibição empilhada
    model = Equipamento
    extra = 0  # Define quantos formulários em branco devem ser exibidos


class CondominioAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['numero_identificacao', 'nome', 'exibir_equipamentos']
    search_fields = ['numero_identificacao', 'nome']
    list_display_links = ['numero_identificacao', 'nome']
    
    

    list_per_page = 10     

    def exibir_equipamentos(self, obj):
        return ', '.join([equipamento.nome for equipamento in obj.equipamentos.all()])
    
    exibir_equipamentos.short_description = 'Equipamentos'


    inlines = [EquipamentoInline]



class ListaEquipamento(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('numero_serie','nome', 'data_instalacao', 'testado',)
    list_display_links = ('numero_serie', 'nome',)
    list_per_page = 10


admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Equipamento, ListaEquipamento)