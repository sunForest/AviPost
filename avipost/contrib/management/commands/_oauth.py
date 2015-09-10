import os

from django.core.management import call_command


def _abs_path(rel_path):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        rel_path
    )


def create():
    """ create user and application """
    path_to_superuser_fixture = _abs_path('user.json')
    path_to_app_fixture = _abs_path('app.json')
    call_command('loaddata', path_to_superuser_fixture)
    call_command('loaddata', path_to_app_fixture)
