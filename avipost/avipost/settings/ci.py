""" 
Complete settings for ci
= ci_stubbed_prod settings  + extra ci environments

"""
from .ci_stubbed_prod import *

INSTALLED_APPS += ('autofixture',)
