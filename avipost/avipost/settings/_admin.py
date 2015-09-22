"""
admin mixin
"""
# TODO not real mixin, base will be excuted multiple times
from .base import *

INSTALLED_APPS += (
    'autofixture',
    'contrib'
)
