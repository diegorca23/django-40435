from django.urls import path
from coder import views

# app_name = 'coder'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('crear-cursos/', views.crear_cursos, name='crear_cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
]