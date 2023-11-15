import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Equipamento, Condominio
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    paginator = Paginator(equipamentos, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "dados/equipamentos.html", {"page_obj" : page_obj})



@login_required
def condominios(request):
    condominios = Condominio.objects.all()
    return render(request, "dados/condominios.html", {"condominios" : condominios})


# @login_required
# def exportar_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="equipamentos.csv"'

#     writer = csv.writer(response)
#     writer.writerow([
#         'Nome',
#         'N Serie',
#         'Descricao',
#         'Condominio'
#     ])

#     equipamentos = Equipamento.objects.all()

#     for equipamento in equipamentos:
#         writer.writerow([
#             equipamento.nome,
#             equipamento.numero_serie,
#             equipamento.descricao,
#             equipamento.condominio
#         ])

#     return response



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



def exportar_equipamentos_csv(request):
    campos = ['nome', 'numero_serie', 'condominio']
    nome_arquivo = 'equipamentos'
    return exportar_csv(request, Equipamento, campos, nome_arquivo)


def exportar_condominio_csv(request):
    campos = ['numero_identificacao', 'nome']
    nome_arquivo = 'condominios'
    return exportar_csv(request, Condominio, campos, nome_arquivo)

# pagina não encontrada
def custom_404(request, exception):
    return render(request, 'error/404.html', {})

