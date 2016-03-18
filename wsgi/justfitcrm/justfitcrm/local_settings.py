from .settings import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '10.50.19.63',
        'PORT': '3306',
    }
}