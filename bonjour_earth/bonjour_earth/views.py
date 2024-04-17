from django.http import HttpResponse
from django.shortcuts import render


def fronthello(request):
    data = {
        "nom":"Rakoto",
        "age":32,
        "taille":1.56,
        "genre":"Homme"
    }
    return render(request, "hello.html",data)

def hello(request, nom):
    return HttpResponse(f"hello Mr/Mdm {nom}")