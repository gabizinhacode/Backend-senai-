from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá, bem-vindo à modelagem da minha biblioteca!")


# Create your views here.
