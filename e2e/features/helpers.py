""" helper functions, mainly those with configuration
or interacting with outside environment """
import subprocess
from collections import namedtuple
import os
from urllib.parse import urljoin


def exec_manage(subcommand, *args):
    """ execute command using manage.py """
    manager = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../../avipost/manage.py'
    )

    cmd = (['python', manager, subcommand] + list(args))

    return subprocess.check_output(cmd).decode().rstrip('\n')


def setup_oauth():
    """ create user and application """
    exec_manage('fixture', '_oauth')


def create_test_user(user_name, token):
    return exec_manage('fixture', '_users', '--par',
                       '{0},{1}'.format(user_name, token))


def clean_db():
    """ clean database """
    exec_manage('flush', '--noinput')


def load_postcards(user_name, count):
    """ load <count> postcards for <user_name>

    :count: integer, e.g. 3

    """
    exec_manage('fixture', '_postcards', '--par',
                '{0},{1}'.format(user_name, count))


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
