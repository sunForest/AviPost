SECRET_KEY = 'w%@7ljsrq9zrajqjh*s(k+tf%qgpasol*vmx8nu&83dz4ft5vz'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'avipost_ci',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}
