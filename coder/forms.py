from django import forms

class CrearCursos(forms.Form):
    comision = forms.CharField(max_length=20)
    lenguaje = forms.CharField(max_length=20)