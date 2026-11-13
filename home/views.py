from django.shortcuts import render, get_object_or_404
from .models import Conteudo, Menu

def obter_menu_ativo():
    """
    Função auxiliar para buscar apenas os itens de menu marcados como 'ativo',
    já ordenados pelo campo 'ordem'.
    """
    return Menu.objects.filter(ativo=True).order_by('ordem')


def home(request):
    """
    View da página inicial (/).
    Busca o menu ativo e tenta encontrar um conteúdo com slug 'inicio' (ou pega o primeiro ativo).
    """
    menu_itens = obter_menu_ativo()
    
    # Procura primeiro por um conteúdo com slug 'inicio' ou 'home'
    conteudo_principal = Conteudo.objects.filter(slug__in=['inicio', 'home'], ativo=True).first()
    
    # Se não houver um com esse slug, pega o primeiro conteúdo ativo cadastrado
    if not conteudo_principal:
        conteudo_principal = Conteudo.objects.filter(ativo=True).first()

    contexto = {
        'menu_itens': menu_itens,
        'conteudo': conteudo_principal,
    }
    return render(request, 'portal/index.html', contexto)


def exibir_conteudo(request, slug):
    """
    View dinâmica (/conteudo/<slug>/).
    Busca o conteúdo correspondente ao slug na URL; se não existir ou estiver inativo, retorna erro 404.
    """
    menu_itens = obter_menu_ativo()
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)

    contexto = {
        'menu_itens': menu_itens,
        'conteudo': conteudo,
    }
    return render(request, 'portal/index.html', contexto)

