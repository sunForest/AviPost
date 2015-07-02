""" helper functions, mainly those with configuration
or interacting with outside environment """
import subprocess
from collections import namedtuple
import os
from urlparse import urljoin


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
    base_path = os.path.dirname(os.path.realpath(__file__))
    path_to_user_fixture = os.path.join(base_path, 'user.json')
    path_to_app_fixture = os.path.join(base_path, 'app.json')
    exec_manage('loaddata', path_to_user_fixture)
    exec_manage('loaddata', path_to_app_fixture)


def clean_db():
    """ clean database """
    exec_manage('flush', '--noinput')


def load_data(model, count):
    """ load <count> models

    :model: name of model, e.g. Postcard
    :count: integer, e.g. 3

    """
    exec_manage(
        'loadtestdata', 'postcards.{0}:{1}'.format(model, count),
        '--overwrite-defaults'
    )


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
        'Helpers', ['url', 'file_path', 'load_data', 'clean_db', 'setup_oauth']
    )(
        url, file_path, load_data, clean_db, setup_oauth
    )
