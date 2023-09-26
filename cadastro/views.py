import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Equipamento
from django.contrib.auth.decorators import login_required



@login_required
def equipamentos(request):

    equipamentos = Equipamento.objects.all()


    return render(request, "dados/equipamentos.html", {"equipamentos" : equipamentos})



@login_required
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="equipamentos.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Nome',
        'N Serie',
        'Descricao',
        'Condominio'
    ])

    equipamentos = Equipamento.objects.all()

    for equipamento in equipamentos:
        writer.writerow([
            equipamento.nome,
            equipamento.numero_serie,
            equipamento.descricao,
            equipamento.condominio
        ])

    return response



def custom_404(request, exception):
    return render(request, 'error/404.html', {})

