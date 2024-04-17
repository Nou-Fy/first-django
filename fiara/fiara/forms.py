from django import forms

from .models import Personne


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ("nom", "prenom", "age", "genre")