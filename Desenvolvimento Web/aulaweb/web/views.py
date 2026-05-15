from django.shortcuts import render
from .models import Produto, Cliente

# Create your views here.

def index(request) :
    return render(request, 'index.html')

def sobre(request):
    return render(request,'sobre.html')

def recuperar_produto(request, id):
    produto = Produto.objects.get(pk=id)
    return render(request, 'produto.html', {'produto': produto})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "listar_produtos.html", {'produtos': produtos})

def detalhar_produto(request, id):
    produto = produto()
    try:
        produto = Produto.objects.get(pk=id)
    except Exception as e:
        produto.nome = "Não existe"
    return render(request, "produto_detail.html", {'produto' : produto})