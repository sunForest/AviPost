"""
Hooks for running tests
"""
from urlparse import urljoin
import behave
import os

from steps._fixture import Fixture


def clean_db(context):
    Fixture(
        context.config.userdata.get('manager')
    ).clean_db()


def get_file_path(file_name):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'files/',
        file_name
    )


def before_all(context):
    context.url = (
        lambda rel: urljoin(context.config.userdata.get('base_url'), rel)
    )
    context.file_path = get_file_path

def before_scenario(context, _):
    clean_db(context)


def after_scenario(context, _):
    clean_db(context)
