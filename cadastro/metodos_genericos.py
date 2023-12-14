from django.db.models import Q
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Author: Kemuel kesley
# Date: 14/12/2023
# Fazer busca de dados no models Condomionios e Equipamentos
def buscar_dados(modelo, nome, busca_1, busca_2):
    if nome:
        query = Q(**{f'{busca_1}__icontains': nome}) | Q(**{f'{busca_2}__icontains': nome})
        return modelo.objects.filter(query)
    else:
        return modelo.objects.all()



# funcao generica para criar paginacao
def criar_paginacao(request, objeto):
    paginator = Paginator(objeto, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj




# funcao generica para criar arquivos csv
@login_required
def exportar_csv(request, modelo, campos, nome_arquivo):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{nome_arquivo}.csv"'

    writer = csv.writer(response)
    writer.writerow(campos)

    objetos = modelo.objects.all()

    for objeto in objetos:
            data = [getattr(objeto, campo) for campo in campos]
            writer.writerow(data)


    return response
