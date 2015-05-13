"""
Hooks for running tests
"""
from urlparse import urljoin
import behave

from steps._fixture import Fixture


def clean_db(context):
    Fixture(
        context.config.userdata.get('manager')
    ).clean_db()


def before_all(context):
    context.url = (
        lambda rel: urljoin(context.config.userdata.get('base_url'), rel)
    )

def before_scenario(context, _):
    clean_db(context)


def after_scenario(context, _):
    clean_db(context)
