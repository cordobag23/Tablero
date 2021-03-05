from django.db import models



class Equipo(models.Model):
    nombre_miembro = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.nombre_miembro
