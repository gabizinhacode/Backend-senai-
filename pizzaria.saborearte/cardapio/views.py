from django.shortcuts import render
from django.http import HttpResponse

def pizza_do_dia(request):
    return HttpResponse("Pizza do dia: Peru")

def promocoes(request):
    return HttpResponse("Promoções: 10% de desconto nas pizzas grandes às terças-feiras")
# Create your views here.
