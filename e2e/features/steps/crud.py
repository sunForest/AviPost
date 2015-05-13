import json

from behave import given, when, then
# implicitly used
import sure
from inflection import singularize
import requests
from json_schema_generator import SchemaGenerator
# We use this instead of validator from json_schema_generator
# because its error reports are far better
from jsonschema import validate

from _fixture import Fixture
from _lazy_request import LazyRequest


# supress requests logging
import logging
logging.getLogger("requests").setLevel(logging.WARNING)


@given('server has {count:d} {item:S}')
def step_impl(context, count, item):
    Fixture(
        context.config.userdata.get('manager')
    ).load_data(singularize(item), count)


@when('GET "{rel_url:S}"')
def step_impl(context, rel_url):
    context.request = LazyRequest('GET', context.url(rel_url))


@when('POST "{rel_url:S}"')
def step_impl(context, rel_url):
    context.request = LazyRequest('POST', context.url(rel_url))


@when('with file "{name:S}" as {field:S}')
def step_impl(context, name, field):
    context.request.add_file(context.file_path(name), field)


@when('with data')
def step_impl(context):
    context.request.add_data(json.loads(context.text))

@then('request will {state:S} for {code:d}')
def step_impl(context, state, code):
    context.response = context.request.send()
    context.response.status_code.should.equal(code)
    if str(code).startswith('2'):
        state.should.equal('success')


@then('return {count:d} items')
def step_impl(context, count):
    assert len(context.response.json()).should.equal(count)


@then('is like')
def step_impl(context):
    schema = SchemaGenerator.from_json(context.text)
    validate(context.response.json(), schema.to_dict())
