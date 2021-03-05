from django.db import models
from applications.proyecto.models import *
from applications.tareas.models import *

class Historias(models.Model):
    como = models.CharField('Como', max_length=50)
    quiero = models.CharField('Quiero', max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tareas = models.ManyToManyField(Tareas)

    def __str__(self):
        return self.como
    
