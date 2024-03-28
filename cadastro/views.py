from django.shortcuts import render
from .models import Equipamento, Condominio
from django.contrib.auth.decorators import login_required

# import metodos_genericos
from .metodos_genericos import buscar_dados
from .metodos_genericos import criar_paginacao
from .metodos_genericos import exportar_csv



@login_required
def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    paginas = criar_paginacao(request, equipamentos)

    nome = request.GET.get('nome')

    if nome:
        equipamentos = buscar_dados(Equipamento, nome, 'nome', 'numero_serie')
        paginas = criar_paginacao(request, equipamentos)

    context = {
        "criar_paginacao": paginas
    }

    return render(request, "dados/equipamentos.html", context)


@login_required
def condominios(request):
    condominios = Condominio.objects.all()
    paginas = criar_paginacao(request, condominios)    
   
    nome = request.GET.get('nome')

    if nome:
        condominios = buscar_dados(Condominio, nome, 'nome', 'numero_identificacao')
        paginas = criar_paginacao(request, condominios)

        
    context = {
        "criar_paginacao" : paginas
    }
    
    return render(request, "dados/condominios.html", context)


# pagina não encontrada
def custom_404(request, exception):
    return render(request, 'error/404.html', {})




def exportar_equipamentos_csv(request):
    campos = ['nome', 'numero_serie', 'condominio']
    nome_arquivo = 'equipamentos'
    return exportar_csv(request, Equipamento, campos, nome_arquivo)


def exportar_condominio_csv(request):
    campos = ['numero_identificacao', 'nome']
    nome_arquivo = 'condominios'
    return exportar_csv(request, Condominio, campos, nome_arquivo)

