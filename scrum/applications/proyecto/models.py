from django.db import models
from applications.equipo.models import *


class Proyecto(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    equipo = models.ManyToManyField(Equipo)

    def __str__(self):
        return self.nombre