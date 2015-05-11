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


# supress requests logging
import logging
logging.getLogger("requests").setLevel(logging.WARNING)


@given('server has {count:d} {item}')
def step_impl(context, count, item):
    Fixture(
        context.config.userdata.get('manager')
    ).load_data(singularize(item), count)


@when('GET "{url:S}"')
def step_impl(context, url):
    base_url = context.config.userdata.get('base_url')
    context.response = requests.get(urljoin(base_url, url))
    print(context.response.text)


@then('request will {:w}({code:d})')
def step_impl(context, _, code):
    context.response.status_code.should.equal(code)


@then('return {count:d} items')
def step_impl(context, count):
    assert len(context.response.json()).should.equal(count)


@then('is like')
def step_impl(context):
    schema = SchemaGenerator.from_json(context.text)
    validate(context.response.json(), schema.to_dict())
