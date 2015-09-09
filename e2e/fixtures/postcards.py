""" Create a complete test data fixture for e2e tests of various clients """

import os

# The script will be run under django context, so linter may report
# false positive warnings. Here we use noqa somewhere to tell pyflake8
# not complain some missing references.
from autofixture import AutoFixture, generators

count = int(os.environ.get('COUNT', 30))

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

user = User.objects.get(username=settings.TEST_CONFIG['USER_NAME'])  # noqa

postcard_fixture = AutoFixture(
    Postcard,  # noqa
    field_values={
        'cover': generators.ChoicesGenerator(values=cover_files),
        'sender': user
    }
)

Postcard.objects.all().delete() # noqa

postcard_fixture.create(count)
