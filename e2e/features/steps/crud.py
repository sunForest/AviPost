import json

from behave import given, when, then
# implicitly used
import sure
# We use this instead of validator from json_schema_generator
# because its error reports are far better
from jsonschema import validate

from _lazy_request import LazyRequest


# supress requests logging
import logging
logging.getLogger("requests").setLevel(logging.WARNING)


@given('I am logged in')
def step_impl(context):
    token = 'fake_token'
    context.helpers.create_test_user(token)
    context.token = token


@given('I received {count:d} postcards')
def step_impl(context, count):
    context.helpers.load_postcards(count)


@when('GET "{rel_url:S}"')
def step_impl(context, rel_url):
    context.request = LazyRequest(
        'GET', context.helpers.url(rel_url), context.token)


@when('POST "{rel_url:S}"')
def step_impl(context, rel_url):
    context.request = LazyRequest(
        'POST', context.helpers.url(rel_url), context.token)


@when('with file "{name:S}" as {field:S}')
def step_impl(context, name, field):
    context.request.add_file(context.helpers.file_path(name), field)


@when('with data')
def step_impl(context):
    context.request.add_data(json.loads(context.text))


@then('request will {state:S} for {code:d}')
def step_impl(context, state, code):
    context.response = context.request.send()
    context.response.status_code.should.equal(code)


@then('return {count:d} items')
def step_impl(context, count):
    print (context.response.json())
    cnt = len(context.response.json())
    cnt.should.equal(count)


@then('has structure')
def step_impl(context):
    validate(context.response.json(), json.loads(context.text))
