from .base import *

ALLOWED_HOSTS = ['138.68.14.229', 'app-bobross.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'adminkld',
#         'USER': 'u_adminkld',
#         'PASSWORD': 'praJfhBh',
#         'HOST': '',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bobross',
        'USER': 'bobross_user',
        'PASSWORD': 'Qxb35A]5>x',
        'HOST': 'localhost',
        'PORT': '',
    }
}
