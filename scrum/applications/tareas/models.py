from django.db import models
from applications.equipo.models import *

class Tareas(models.Model):
    descripcion = models.CharField('Descripción de la tarea', max_length=50)
    equipo_tarea = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    estado = models.CharField('Estado de la tarea', max_length=50)

    def __str__(self):
        return self.descripcion