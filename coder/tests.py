import random
import string

from django.test import TestCase
from coder.models import Curso

class CursoTestCase(TestCase):

    def test_creacion_cursos(self):
        # Test 1: Comprobar puedo crear un curso con un nombre con letras random
        lista_letras_comision = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_lenguaje = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        comision_prueba = "".join(lista_letras_comision)
        lenguaje_prueba = "".join(lista_letras_lenguaje)
        
        
        curso_1 = Curso.objects.create(comision=comision_prueba, lenguaje=lenguaje_prueba)

        self.assertIsNotNone(curso_1.id)
        self.assertEqual(curso_1.comision, comision_prueba)
        self.assertEqual(curso_1.lenguaje, "Diego")