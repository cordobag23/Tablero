#ayuda sacar la informacion de¿j archivo json 
#para que nadie tenga acceso  a los datos del servidor
from django.core.exceptions import ImproperlyConfigured
import json



#************INICIO***ESTO LO CAMBIAMOS POR LA CONFIG. DEL UNIPATH***********#
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)
#************FIN***ESTO LO CAMBIAMOS POR LA CONFIG. DEL UNIPATH***********#


# llave secreta para utilizar el proyecto en PRODUCCION
#abrimos  el archivo json
with open("secret.json") as f: 
    secret = json.loads(f.read())

#funcion q esconde la info 
def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)

SECRET_KEY = get_secret('SECRET_KEY')


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     
)

#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmejorandooooooooooooooooooooooooooooo
#aqui las aplicaciones locales 
LOCAL_APPS = (
    'applications.equipo', 
    'applications.proyecto', 
    'applications.historias', 
    'applications.tareas', 
    'applications.revision', 
    'applications.impedimentos', 
    'applications.users',
)

#aqui aplicaicones de terceros
THIRD_PARTY_APPS = ()

#concatenamos todas las apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

###ffffffffffffffffiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scrum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
# CONF. para q la ruta d los templates este directamnt en la rama principal
#pasa de 'DIRS': []   a:   
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'scrum.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

###nnnnnnnnnnnnnnnnuuuuuuuuuuuuuuueeeeeeeeeevooooooooooooooooooo
#le indico q todo el project trabaje bajo mi modelo USERS

AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True