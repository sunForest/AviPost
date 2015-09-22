"""
Production settings with some stubbed components in ci environment, like database.
Besides these stubs the settings are as similar to production as possible

Mainly used by service in docker on ci server

"""
from .base import *
from ._ci import *
