"""
Hooks for running tests
"""
from helpers import helpers


def before_all(context):
    # hook helper functions
    context.helpers = helpers(context)


def before_scenario(context, _):
    context.helpers.clean_db()


def after_scenario(context, _):
    context.helpers.clean_db()
