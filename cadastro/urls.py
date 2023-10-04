from django.urls import path
from cadastro.views import  exportar_csv, equipamentos, condominios, exportar_equipamentos_csv, exportar_condominio_csv


urlpatterns = [
    path("exportar_csv", exportar_csv, name="exportar_csv"),
    path("equipamentos", equipamentos, name="equipamentos"),
    path("condominios", condominios, name="condominios"),
    path("exportar_equipamentos_csv", exportar_equipamentos_csv, name="exportar_equipamentos_csv"),
    path("exportar_condominio_csv", exportar_condominio_csv, name="exportar_condominio_csv"),
]
