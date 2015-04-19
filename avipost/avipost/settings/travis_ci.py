from .base import *

SECRET_KEY = 'w%@7ljsrq9zrajqjh*s(k+tf%qgpasol*vmx8nu&83dz4ft5vz'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'travis_ci_test',
        'ATOMIC_REQUESTS': True,
    }
}
