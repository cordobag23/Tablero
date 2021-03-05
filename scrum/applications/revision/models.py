from django.db import models
from applications.historias.models import *
from applications.tareas.models import *
from applications.equipo.models import *
from applications.impedimentos.models import *


class Revision(models.Model):
    
    nombre = models.CharField('Nombre de la revision', max_length=50)
    equipo_rev = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    historia = models.ForeignKey(Historias, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE)
    que_ha_hecho = models.CharField('Qué ha hecho', max_length=500, blank=True, null=True)
    que_ha_hara = models.CharField('Qué ha hará', max_length=500, blank=True, null=True)
    comentarios = models.CharField('Comentarios', max_length=500, blank=True, null=True)
    impedimentos = models.ForeignKey(Impedimentos, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

