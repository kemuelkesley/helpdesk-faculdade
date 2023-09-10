from django.contrib import admin

from cadastro.models import Condominio, Equipamento


class Listacondominio(admin.ModelAdmin):
   list_display = ('numero_identificacao','nome',)
   list_filter = ('numero_identificacao', 'nome',)
   list_per_page = 10



class ListaEquipamento(admin.ModelAdmin):
    list_display = ('numero_serie','nome', 'data_instalacao',)
    list_display_links = ('numero_serie', 'nome',)
    list_per_page = 10
    


admin.site.register(Condominio, Listacondominio)
admin.site.register(Equipamento, ListaEquipamento)


