from django.urls import path
from cadastro.views import equipamentos, exportar_csv


urlpatterns = [
    path("equipamentos", equipamentos, name="equipamentos"),
    path("exportar_csv", exportar_csv, name="exportar_csv"),
]