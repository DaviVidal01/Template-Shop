from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    Produtos = RoupaPromo.objects.all()
    carousel = Carrossel.objects.all() 
    icons = Icons.objects.all() 
    img = Imagens.objects.all()
    depoimentos = Depoimentos.objects.all()    
    return render(request,'index.html',{"products": Produtos, "carousel": carousel, "icons": icons, "imagens": img, "depoimentos": depoimentos })

def produtos(request):
    RPromo = RoupaPromo.objects.all()
    RCasual = RoupaCasual.objects.all()
    RSocial = RoupaSocial.objects.all()
    carousel = Carrossel.objects.all() 
    icons = Icons.objects.all() 
    img = Imagens.objects.all()
    return render(request,'produtos.html', {"carousel": carousel, "icons": icons, "imagens": img, "promo": RPromo, "casual": RCasual, "social": RSocial})

def carrinho(request):
    return render(request,'carrinho.html')

def teste(request):
    all_entries = Roupa.objects.all()
    retorno = all_entries
    #all_entries = Site.objects.get(id=5)
    #retorno = all_entries.nome_produto + " | " + all_entries.description + " | "
    return HttpResponse(retorno)

