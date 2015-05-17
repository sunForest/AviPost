""" Create a complete test data fixture for e2e tests of various clients """

# The script will be run under django context, so linter may report
# false positive warnings. Here we use noqa somewhere to tell pyflake8
# not complain some missing references.
from autofixture import AutoFixture, generators
from django.core.management import call_command

cover_files = (
    'covers/demo-horizontal.png',
    'covers/demo-horizontal-2.jpg',
    'covers/demo-horizontal-3.jpg',
    'covers/demo-horizontal-4.jpg',
    'covers/demo-square.jpg',
    'covers/demo-vertical.jpg',
    'covers/demo-vertical-2.jpg',
    'covers/placeholder.jpg',
)

postcard_fixture = AutoFixture(
    Postcard,  # noqa
    field_values={
        'cover': generators.ChoicesGenerator(values=cover_files),
    }
)

call_command('flush', interactive=False)

postcard_fixture.create(30)
