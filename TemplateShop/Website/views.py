from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def produtos(request):
    return render(request,'produtos.html')

def carrinho(request):
    return render(request,'carrinho.html')