import json
from urlparse import urljoin

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


@given('server has (?P<count>\d+) (?P<item>\S+)')
def step_impl(context, count, item):
    Fixture(
        context.config.userdata.get('manager')
    ).load_data(singularize(item), count)


@when('(?P<verb>GET|POST|PUT|DEL) "(?P<rel_url>/\S+)"')
def step_impl(context, verb, rel_url):
    base_url = context.config.userdata.get('base_url')
    context.request = LazyRequest(verb, urljoin(base_url, rel_url))


@when('with file "(?P<name>\S+)" as (?P<field>\S+)')
def step_impl(context, name, field):
    context.request.add_file(name, field)


@when('with data')
def step_impl(context):
    context.request.add_data(json.loads(context.text))

@then('request will (?P<state>\S+) for (?P<code>\d+)')
def step_impl(context, state, code):
    context.response = context.request.send()
    context.response.status_code.should.equal(int(code))
    if code.startswith('2'):
        state.should.equal('success')


@then('return (?P<count>\d+) items')
def step_impl(context, count):
    assert len(context.response.json()).should.equal(int(count))


@then('is like')
def step_impl(context):
    schema = SchemaGenerator.from_json(context.text)
    validate(context.response.json(), schema.to_dict())
