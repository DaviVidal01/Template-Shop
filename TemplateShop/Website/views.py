from django.shortcuts import render
from django.http import HttpResponse
from .models import Site
# Create your views here.

def index(request):
    all_products = Site.objects.all()
    return render(request,'index.html', {"products": all_products})

def produtos(request):
    return render(request,'produtos.html')

def carrinho(request):
    return render(request,'carrinho.html')

def teste(request):
    all_entries = Site.objects.all()
    retorno = all_entries
    #all_entries = Site.objects.get(id=5)
    #retorno = all_entries.nome_produto + " | " + all_entries.description + " | "
    return HttpResponse(retorno)