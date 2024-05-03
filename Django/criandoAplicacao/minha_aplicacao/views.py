# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página inicial do site")

def sobre(request):
    return HttpResponse("Página Sobre")

def contato(request):
    return HttpResponse("Página de Contato")
