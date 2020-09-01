from django.shortcuts import render
from .models import Enquete

def index(request):
    return render(request, 'bemvindo.html')

def enquete(request, enquete_id):
    context = {}
    if enquete_id == 1:
        context['enquete'] = Enquete("Como usar orientação a objetos em Java?", '2020-08-26')
    elif enquete_id == 2:
        context['enquete'] = Enquete("O que é C ou C++", '2020-07-30') 
    elif enquete_id == 3:
        context['enquete'] = Enquete("O que é debugar?", '2020-08-16')
    return render(request, 'enquete.html', context)
