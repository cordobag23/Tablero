from django.db import models

# importamos para heedar o sobreescribir metodos de creacion y manioulación de usuarios
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#importamos el user manager:
from .managers import UserManager

#modelos,,, el PermissionsMixin le indica a django a 
#bamos a controlar todo lo correspondiente a usuarios

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=40, blank=True)
    apellidos = models.CharField(max_length=40, blank=True)
    is_staff = models.BooleanField(default=False)

    #le indico con q field uiero q inicie sesion en el admin tareas

    USERNAME_FIELD = 'username'

    #para q me pida el email al crear el USUARIO
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
