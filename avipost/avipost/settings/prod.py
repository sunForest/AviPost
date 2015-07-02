from .base import *

INSTALLED_APPS += (
    'corsheaders',
)

# need to be before django.middleware.common.CommonMiddleware
MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
) + MIDDLEWARE_CLASSES

CORS_ORIGIN_ALLOW_ALL = True

# TODO: set the database parameters

ALLOWED_HOSTS = ["52.16.214.13", "127.0.0.1", "localhost"]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'postgres',
#         'USER': 'postcard_admin',
#         'PASSWORD': get_env_variable('DB_PASSWORD'),
#         'HOST': 'postcarddb.cqlnuay9niw1.eu-west-1.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# }

#SECRET_KEY = get_env_variable('SECRET_KEY')
