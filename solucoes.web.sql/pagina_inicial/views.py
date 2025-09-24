from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá, bem-vindo a soluções web rapidas! Em breve , um novo site para impulsionar seu negocio.")

# Create your views here.
