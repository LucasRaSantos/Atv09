from django.shortcuts import render
from .models import Conteudo

def home_menu(request):
    conteudos = {
        "Conteudo":Conteudo.objects.all()
    }
    return render(request, 'index.html', conteudos)
