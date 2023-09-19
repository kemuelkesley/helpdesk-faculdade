from django.contrib import admin

from cadastro.models import Condominio, Equipamento


# class Listacondominio(admin.ModelAdmin):
#    list_display = ('numero_identificacao','nome',)
#    list_filter = ('numero_identificacao', 'nome',)
#    list_per_page = 10



class ListaEquipamento(admin.ModelAdmin):
    list_display = ('numero_serie','nome', 'data_instalacao',)
    list_display_links = ('numero_serie', 'nome',)
    list_per_page = 10
    


# admin.site.register(Condominio, Listacondominio)
admin.site.register(Equipamento, ListaEquipamento)


class EquipamentoInline(admin.StackedInline):  # Use admin.StackedInline para uma exibição empilhada
    model = Equipamento
    extra = 0  # Define quantos formulários em branco devem ser exibidos


class CondominioAdmin(admin.ModelAdmin):
    list_display = ['numero_identificacao', 'nome', 'exibir_equipamentos']

    def exibir_equipamentos(self, obj):
        return ', '.join([equipamento.nome for equipamento in obj.equipamentos.all()])
    
    exibir_equipamentos.short_description = 'Equipamentos'


    inlines = [EquipamentoInline]



admin.site.register(Condominio, CondominioAdmin)