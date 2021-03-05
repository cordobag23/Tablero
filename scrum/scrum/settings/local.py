#************INICIO***ESTO LO iomprtamos***********#
from .base import *
DEBUG = True

ALLOWED_HOSTS = []

#************FIN***ESTO LO importamos***********#


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# cimomo ya esta importadp el base.local ya esta la funcion q esconde los dats del servidor
#ahora la llamamos y reemplazamos


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':'localhost',
        'PORT':3306
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
