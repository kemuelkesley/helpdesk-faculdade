import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Equipamento, Condominio
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q




@login_required
def equipamentos(request):
    equipamentos = Equipamento.objects.all()
   
    criar_paginacao(request, equipamentos)
    return render(request, "dados/equipamentos.html", {"criar_paginacao" : criar_paginacao(request, equipamentos)})


@login_required
def condominios(request):
    condominios = Condominio.objects.all()
        
    paginas = criar_paginacao(request, condominios)

    buscar_dados(request.GET.get('nome'))
    if request.GET.get('nome'):
        paginas = criar_paginacao(request, buscar_dados(request.GET.get('nome')))

        
    context = {
        "criar_paginacao" : paginas
    }
    
    return render(request, "dados/condominios.html", context)


# funcao para filtrar dados
def buscar_dados(nome):
    if nome:
        return Condominio.objects.filter(
            Q(numero_identificacao__icontains=nome) | Q(nome__icontains=nome))
    
    else:        
        return Condominio.objects.all()
    

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

