from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.edad} años'
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    comision= models.CharField(max_length=20)
    lenguaje = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.comision} - {self.lenguaje}'