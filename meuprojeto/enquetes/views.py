from django.shortcuts import render
from enquetes.models import Enquete

def index(request):
    return render(request, 'bemvindo.html')

def mostrar(request, enquete_id):
    e = Enquete.objects.get(id=enquete_id)
    return render(request, 'enquete.html', {'enquete': e})