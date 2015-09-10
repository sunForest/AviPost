""" Create a complete test data fixture for e2e tests of various clients """

from autofixture import AutoFixture, generators
from postcards.models import Postcard
from django.contrib.auth.models import User
from django.conf import settings


def create(username, count=30):
    count = int(count)
    # count = int(os.environ.get('COUNT', 30))

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

    # user = User.objects.get(username=username)
    user = User.objects.get(username=settings.TEST_CONFIG['USER_NAME'])

    postcard_fixture = AutoFixture(
        Postcard,
        field_values={
            'cover': generators.ChoicesGenerator(values=cover_files),
            'sender': user
        }
    )

    clean()

    postcard_fixture.create(count)


def clean():
    Postcard.objects.all().delete()
