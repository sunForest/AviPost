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
