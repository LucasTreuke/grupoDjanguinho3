from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

# Create your views here.
def index(request):
    return HttpResponse("<a href='special'>Special</a><br><a href='pontos'>pontos</a><br><a href='bacon'>bacon</a><br><strong>Coé</strong>")

def redireciona(request):
    url = reverse("bacon")
    return HttpResponseRedirect(url)

def view_dinamica_int(request,param):
    if param == 0:
        return HttpResponse("<strong>ALO</strong>")
    elif param == 1:
        return HttpResponse("<strong>ALO2</strong>")


def special(request):
    return render(request,"treuke/truco.html")

def pontos(request):
    return render(request,"treuke/exercicio_pontos.html")

def bacon(request):
    context = {
        "nome":"samplenamehere",
        "list":["a","b","c"],
        "string_espacada":"AA    aaa  loo oo",
        "valor":""
    }
    return render(request,"treuke/bacon.html",context)