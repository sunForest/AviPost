""" 
Complete settings for ci
= ci_stubbed_prod settings  + extra ci environments

"""
from .ci_stubbed_prod import *

CORS_ORIGIN_ALLOW_ALL = True
INSTALLED_APPS += ('autofixture',)
