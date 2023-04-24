from django.shortcuts import render, redirect
from coder.models import Curso
from coder.forms import CrearCursos

def inicio(request):
    return render(request, 'index.html')

def prueba_render(request):
    datos = {'nombre': 'Pepe'}
    return render(request, 'prueba_render.html', datos)

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def crear_cursos(request):
    if request.method == "POST":
        formulario = CrearCursos(request.POST)

        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data

            curso = Curso(comision=datos_correctos['comision'], lenguaje=datos_correctos['lenguaje'])
            curso.save()

            return redirect('cursos')
    
    formulario = CrearCursos()
    return render(request, 'crear_cursos.html', {'formulario': formulario})


def estudiantes(request):
    return render(request, 'estudiantes.html')

def profesores(request):
    return render(request, 'profesores.html')