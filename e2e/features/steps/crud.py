import json
import re

from behave import given, when, then
from behave import use_step_matcher
use_step_matcher("re")
# implicitly used
import sure  # noqa
# We use this instead of validator from json_schema_generator
# because its error reports are far better
from jsonschema import validate

from _lazy_request import LazyRequest


# supress requests logging
import logging
logging.getLogger("requests").setLevel(logging.WARNING)


# (?:xx) changes priority but will not be captured as args
@given('(.+) are users')
def step_impl(context, user_names_str):
    if not hasattr(context, 'users'):
        context.users = {}

    user_names = [name.strip() for name in re.split('and|,', user_names_str)]
    for user_name in user_names:
        token = 'fake_token_' + user_name
        user_id = context.helpers.create_test_user(user_name, token)
        context.users[user_name] = {'token': token, 'id': user_id}


@given('(\w+) (?:is|am|are) logged in')
def step_impl(context, user_name):
    context.token = context.users[user_name]['token']


@given('(\w+) received (\d+) postcards')
def step_impl(context, user_name, count):
    context.helpers.load_postcards(user_name, count)


@when('GET "(\S+)"')
def step_impl(context, rel_url):
    context.request = LazyRequest(
        'GET', context.helpers.url(rel_url), context.token)


@when('POST "(\S+)"')
def step_impl(context, rel_url):
    context.request = LazyRequest(
        'POST', context.helpers.url(rel_url), context.token)


@when('with file "(\S+)" as (\w+)')
def step_impl(context, name, field):
    context.request.add_file(context.helpers.file_path(name), field)


@when('with data')
def step_impl(context):
    data = json.loads(context.text)
    receiver_name = re.match(r"\<(\w+)'s id\>", data['receiver']).group(1)
    data['receiver'] = context.users[receiver_name]['id']
    context.request.add_data(data)


@then('request will (\w+) for (\d+)')
def step_impl(context, state, code):
    context.response = context.request.send()
    context.response.status_code.should.equal(int(code))


@then('return (\d+) items')
def step_impl(context, count):
    cnt = len(context.response.json())
    cnt.should.equal(int(count))


@then('has structure')
def step_impl(context):
    validate(context.response.json(), json.loads(context.text))
