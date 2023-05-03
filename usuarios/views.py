from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            return redirect('inicio')
        else:
            return render(request, 'usuarios/login.html', {'formulario': formulario})
            
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        # formulario = MiFormularioDeCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})
            
    
    formulario = UserCreationForm()
    # formulario = MiFormularioDeCreacion()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})