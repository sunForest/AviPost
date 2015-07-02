import json

from behave import given, when, then
# implicitly used
import sure
from inflection import singularize
from json_schema_generator import SchemaGenerator
# We use this instead of validator from json_schema_generator
# because its error reports are far better
from jsonschema import validate

from _lazy_request import LazyRequest


# supress requests logging
import logging
logging.getLogger("requests").setLevel(logging.WARNING)

IS_LOGGED_IN_USER = False


@given('server has {count:d} {item:S}')
def step_impl(context, count, item):
    context.helpers.load_data(singularize(item), count)


@given('user is logged in')
def step_impl(context):
    global IS_LOGGED_IN_USER
    IS_LOGGED_IN_USER = True


@when('GET "{rel_url:S}"')
def step_impl(context, rel_url):
    context.request = LazyRequest('GET', context.helpers.url(rel_url))
    if IS_LOGGED_IN_USER:
        context.request.get_token()


@when('POST "{rel_url:S}"')
def step_impl(context, rel_url):
    context.request = LazyRequest('POST', context.helpers.url(rel_url))
    if IS_LOGGED_IN_USER:
        context.request.get_token()


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


@then('is like')
def step_impl(context):
    schema = SchemaGenerator.from_json(context.text)
    validate(context.response.json(), schema.to_dict())
