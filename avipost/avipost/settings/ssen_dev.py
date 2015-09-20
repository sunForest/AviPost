from ._dev import *

SECRET_KEY = 'lt$#a29ayf(z(xa*f$$%2ydteo!&ra)$ceiul&y1$9ha*xp0a6'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'avipost2',
        'USER': 'geodjango',
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
