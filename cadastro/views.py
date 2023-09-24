from django.shortcuts import render
from .models import Equipamento



def equipamentos(request):

    equipamentos = Equipamento.objects.all()


    return render(request, "dados/equipamentos.html", {"equipamentos" : equipamentos})


