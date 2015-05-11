"""
Hooks for running tests
"""
from steps._fixture import Fixture

def clean_db(context):
    Fixture(
        context.config.userdata.get('manager')
    ).clean_db()

def before_scenario(context, _):
    clean_db(context)
    
def after_scenario(context, _):
    clean_db(context)
