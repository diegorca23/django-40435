from django.contrib import admin

from coder.models import Curso, Profesor, Estudiante

# admin.site.register(Curso)
# admin.site.register(Profesor)
# admin.site.register(Estudiante)

admin.site.register([Curso, Profesor, Estudiante])