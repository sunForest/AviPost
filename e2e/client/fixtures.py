""" Create a complete test data fixture for e2e tests of various clients """

# The script will be run under django context, so linter may report
# false positive warnings. Here we use noqa somewhere to tell pyflake8
# not complain some missing references.
from autofixture import AutoFixture, generators
from django.core.management import call_command

default_cover_sizes = (
    (800, 600),
    (600, 800),
    (1200, 600),
    (600, 1200),
    (1000, 1000),
)

postcard_fixture = AutoFixture(
    Postcard,  # noqa
    field_values={
        'cover': generators.ImageGenerator(sizes=default_cover_sizes),
    }
)

call_command('flush', interactive=False)

postcard_fixture.create(30)
