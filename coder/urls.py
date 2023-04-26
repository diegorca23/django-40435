from django.urls import path
from coder import views

# app_name = 'coder'

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # CURSOS
    # path('cursos/', views.listar_cursos, name='cursos'),
    # path('cursos/crear/', views.crear_cursos, name='crear_cursos'),
    # path('cursos/<int:id_curso>/', views.detalle_cursos, name='mostrar_cursos'),
    # path('cursos/<int:id_curso>/modificar/', views.modificar_cursos, name='modificar_cursos'),
    # path('cursos/<int:id_curso>/eliminar/', views.eliminar_cursos, name='eliminar_cursos'),

    # ESTUDIANTES
    path('estudiantes/', views.listar_estudiantes, name='estudiantes'),
    path('estudiantes/crear/', views.crear_estudiantes, name='crear_estudiantes'),
    path('estudiantes/<int:id_estudiante>/', views.detalle_estudiantes, name='mostrar_estudiantes'),
    path('estudiantes/<int:id_estudiante>/modificar/', views.modificar_estudiantes, name='modificar_estudiantes'),
    path('estudiantes/<int:id_estudiante>/eliminar/', views.eliminar_estudiantes, name='eliminar_estudiantes'),

    # PROFESORES
    path('profesores/', views.listar_profesores, name='profesores'),


    ### CBV p/ CURSOS
    path('cursos/', views.ListaCursos.as_view(), name='cursos'),
    path('cursos/crear/', views.CrearCurso.as_view(), name='crear_cursos'),
    path('cursos/<int:pk>/', views.MostrarCurso.as_view(), name='mostrar_cursos'),
    path('cursos/<int:pk>/modificar/', views.ModificarCurso.as_view(), name='modificar_cursos'),
    path('cursos/<int:pk>/eliminar/', views.EliminaCurso.as_view(), name='eliminar_cursos'),
]