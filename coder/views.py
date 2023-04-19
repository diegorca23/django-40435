from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def prueba_render(request):
    datos = {'nombre': 'Pepe'}
    return render(request, 'prueba_render.html', datos)