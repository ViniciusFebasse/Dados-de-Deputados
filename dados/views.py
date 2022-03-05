from django.shortcuts import render
from deputados import Deputados

Deputados().requisicao()


def index(request):
    return render(request, 'dados/index.html')
