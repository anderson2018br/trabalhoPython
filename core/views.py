from django.shortcuts import render

# Create your views here.
from core.models import Produto
from django.http import HttpResponse

def getProdutoValor(request):
    idProduto = request.GET.get('idProduto');
    produto = Produto.objects.get(id=idProduto)
    return HttpResponse(produto.preco)
