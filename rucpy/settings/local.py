from base import *
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = { 'default': 
    {'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'ruc', 
    'USER': 'postgres', 
    'PASSWORD': 'postgres', 
    'HOST': '127.0.0.1' } 
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a9vgq(*4s4g@)o7c5vj7vg3fon403^jza12!mr&=o)fyamaf$5'