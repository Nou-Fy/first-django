import django.http
from django.shortcuts import render

from .forms import PersonneForm
from .models import Personne
from django.http import HttpResponse


def authentification(request):
    return render(request, "authentification.html")


def suppr_personne(request, id):
    Personne.objects.filter(id=id).first().delete()
    return HttpResponse("suppression réussie")

def inscription_proprietaire(request):
    if request.method == "POST":
        data = PersonneForm(request.POST)

        if data.is_valid():
            nom_form = data.cleaned_data.get("nom")
            prenom_form = data.cleaned_data.get("prenom")
            age_form = data.cleaned_data.get("age")
            peronne = Personne.objects.create(nom=nom_form, prenom=prenom_form, age=age_form)
            peronne.save()
            return HttpResponse("Ajout Réussi")
        return HttpResponse("Ajout echec")

    else:
        context = {
            "title": "personne",
            "form": PersonneForm(),
            "personne": Personne.objects.all()
        }
        return render(request, "create_personne.html", context)


def profil_proprietaire(request):
    return render(request, "profil_personne.html")


def ajoute_auto(request):
    return render(request, "create_vehicule.html")


def profil_vehicule(request):
    return render(request, "apropos_vehicule.html")


def personnes_ajout(request):
    olona = Personne.objects.create(nom="Link", prenom="Fiary", age=1, genre="Homme")
    olona.save()
    return HttpResponse(olona)
