from django.urls import path
from cadastro.views import equipamentos


urlpatterns = [
    path("equipamentos", equipamentos, name="equipamentos")
]