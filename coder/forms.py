from django import forms


class CrearCursos(forms.Form):
    comision = forms.CharField(max_length=20)
    lenguaje = forms.CharField(max_length=20)

class ModificarCursos(forms.Form):
    comision = forms.CharField(max_length=20)
    lenguaje = forms.CharField(max_length=20)


class CrearEstudiantes(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class ModificarEstudiantes(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()