from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    lenguaje = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()