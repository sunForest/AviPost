from behave import given, when, then

@given('server knows something')
def step_impl(context):
    pass

@when('GET postcards/')
def step_impl(context):
    assert True is not False

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
