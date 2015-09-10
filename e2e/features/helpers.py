""" helper functions, mainly those with configuration
or interacting with outside environment """
import subprocess
from collections import namedtuple
import os
from urllib.parse import urljoin


def _abs_path(rel_path):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        rel_path
    )


def exec_manage(subcommand, *args):
    """ execute command using manage.py """
    manager = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../../avipost/manage.py'
    )

    cmd = (['python', manager, subcommand] + list(args))

    devnull = open(os.devnull, 'w')
    subprocess.call(cmd, stdout=devnull)


def setup_oauth():
    """ create user and application """
    path_to_superuser_fixture = _abs_path('user.json')
    path_to_app_fixture = _abs_path('app.json')
    exec_manage('loaddata', path_to_superuser_fixture)
    exec_manage('loaddata', path_to_app_fixture)


def create_test_user(token):
    exec_manage('fixture', '_users')


def clean_db():
    """ clean database """
    exec_manage('flush', '--noinput')


def load_postcards(count):
    """ load <count> postcards

    :count: integer, e.g. 3

    """
    exec_manage('fixture', '_postcards', '--par',
                '{0},{1}'.format('a', count))


def file_path(file_name):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'files/',
        file_name
    )


def helpers(context):
    def url(rel_url):
        return urljoin(context.config.userdata.get('base_url'), rel_url)

    return namedtuple(
        'Helpers', [
            'url', 'file_path', 'load_postcards',
            'clean_db', 'setup_oauth', 'create_test_user']
    )(
        url, file_path, load_postcards, clean_db, setup_oauth, create_test_user
    )
