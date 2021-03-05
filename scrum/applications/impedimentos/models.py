from django.db import models
from applications.equipo.models import *

# Create your models here.
class Impedimentos(models.Model):
    descripcion = models.CharField('Descripoción', max_length=500)
    equipo_ayuda = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion