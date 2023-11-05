from django.contrib import admin
from cadastro.models import Condominio, Equipamento, CategoriaEquipamento
from import_export.admin import ImportExportModelAdmin


# Use admin.StackedInline para uma exibição empilhada
class EquipamentoInline(admin.TabularInline):
    model = Equipamento   
    extra = 1  


class CategoriaEquipamentoInline(admin.TabularInline):
    model = Equipamento
    extra = 1



class CondominioAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['numero_identificacao', 'nome', 'exibir_equipamentos']
    search_fields = ['numero_identificacao', 'nome']
    list_display_links = ['numero_identificacao', 'nome']   

    list_per_page = 10     

    def exibir_equipamentos(self, obj):
        return ', '.join([equipamento.nome for equipamento in obj.equipamentos.all()])
    
    exibir_equipamentos.short_description = 'Equipamentos'

    exibir_equipamentos.admin_order_field = 'equipamentos__nome'


    inlines = [EquipamentoInline]



class ListaEquipamento(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('numero_serie','nome', 'data_instalacao', 'testado',)
    list_display_links = ('numero_serie', 'nome',)
    
    actions = ['link_csv']
    
    list_per_page = 15


class categoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo' ,'nome', 'quantidade_de_equipamentos',)
    search_fields = ('codigo' ,'nome',)
    list_display_links = ('codigo' ,'nome',)
    

    def quantidade_de_equipamentos(self, obj):
        return obj.equipamentos.count()  

    quantidade_de_equipamentos.short_description = 'Quantidade de Equipamentos'  # Nome exibido na coluna
    

    list_per_page = 15

    inlines = [CategoriaEquipamentoInline]


admin.site.register(CategoriaEquipamento, categoriaAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Equipamento, ListaEquipamento)