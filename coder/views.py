from coder.forms import (CrearCursos, CrearEstudiantes, ModificarCursos,
                         ModificarEstudiantes)
from coder.models import Curso, Estudiante
from django.shortcuts import redirect, render
# Imports para CBV
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def inicio(request):
    return render(request, 'index.html')

def prueba_render(request):
    datos = {'nombre': 'Pepe'}
    return render(request, 'prueba_render.html', datos)

### CURSOS ###
def listar_cursos(request):
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
    return render(request, 'cursos_crear.html', {'formulario': formulario})

def detalle_cursos(request, id_curso):
    curso_a_mostrar = Curso.objects.get(id=id_curso)
    return render(request, 'cursos_mostrar.html', {'curso_a_mostrar': curso_a_mostrar})

def eliminar_cursos(request, id_curso):
    curso_a_eliminar = Curso.objects.get(id=id_curso)
    curso_a_eliminar.delete()
    return redirect('cursos')

def modificar_cursos(request, id_curso):
    curso_a_modificar = Curso.objects.get(id=id_curso)
    
    if request.method == "POST":
        formulario = ModificarCursos(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            
            curso_a_modificar.comision = data_limpia['comision']
            curso_a_modificar.lenguaje = data_limpia['lenguaje']
            curso_a_modificar.save()
            
            return redirect('cursos')
        else:
            return render(request, 'cursos_modificar.html', {'formulario': formulario, 'id_curso': id_curso})
    
    formulario = ModificarCursos(initial={'comision': curso_a_modificar.comision, 'lenguaje': curso_a_modificar.lenguaje})
    return render(request, 'cursos_modificar.html', {'formulario': formulario, 'id_curso': id_curso})


### ESTUDIANTES ###
def crear_estudiantes(request):
    if request.method == "POST":
        formulario = CrearEstudiantes(request.POST)

        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data

            estudiante = Estudiante(nombre=datos_correctos['nombre'], edad=datos_correctos['edad'])
            estudiante.save()

            return redirect('estudiantes')
    
    formulario = CrearEstudiantes()
    return render(request, 'estudiantes_crear.html', {'formulario': formulario})

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiantes(request, id_estudiante):
    estudiante_a_mostrar = Estudiante.objects.get(id=id_estudiante)
    return render(request, 'estudiantes_mostrar.html', {'estudiante_a_mostrar': estudiante_a_mostrar})

def eliminar_estudiantes(request, id_estudiante):
    estudiante_a_eliminar = Estudiante.objects.get(id=id_estudiante)
    estudiante_a_eliminar.delete()
    return redirect('estudiantes')

def modificar_estudiantes(request, id_estudiante):
    estudiante_a_modificar = Estudiante.objects.get(id=id_estudiante)
    
    if request.method == "POST":
        formulario = ModificarEstudiantes(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            
            estudiante_a_modificar.nombre = data_limpia['nombre']
            estudiante_a_modificar.edad = data_limpia['edad']
            estudiante_a_modificar.save()
            
            return redirect('estudiantes')
        else:
            return render(request, 'estudiantes_modificar.html', {'formulario': formulario, 'id_estudiante': id_estudiante})
    
    formulario = ModificarEstudiantes(initial={'nombre': estudiante_a_modificar.nombre, 'edad': estudiante_a_modificar.edad})
    return render(request, 'estudiantes_modificar.html', {'formulario': formulario, 'id_estudiante': id_estudiante})

### PROFESORES ###
def listar_profesores(request):
    return render(request, 'profesores.html')


### ### ###
#  CLASES BASADAS EN VISTAS p/ CURSOS
### ### ### 

class ListaCursos(ListView):
    model = Curso
    template_name = 'cbv/cursos/cursos.html'

class CrearCurso(CreateView):
    model = Curso
    template_name = 'cbv/cursos/cursos_crear.html'
    success_url = '/cursos/'
    fields = ['comision', 'lenguaje']

class MostrarCurso(DetailView):
    model = Curso
    template_name = 'cbv/cursos/cursos_mostrar.html'

class ModificarCurso(UpdateView):
    model = Curso
    template_name = 'cbv/cursos/cursos_modificar.html'
    success_url = '/cursos/'
    fields = ['comision', 'lenguaje']

class EliminaCurso(DeleteView):
    model = Curso
    template_name = 'cbv/cursos/cursos_eliminar.html'
    success_url = '/cursos/'