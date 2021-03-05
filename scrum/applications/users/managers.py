#redefinimos AbstractBaseUser, PermissionsMixin para admin users
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    #puede o no acceder al admin y si es o no un supoer user
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        #encripto la passwod
        user.set_password(password)
        user.save(using=self.db)
        return user




#redefinimos o sobreescribimos a funcion user, crear usuario
    def create_user(self, username, email, password=None, **extra_fields ):
        return self._create_user(username, email, password, False, False, **extra_fields )

#redefinimos cear super usuario
    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields )


    