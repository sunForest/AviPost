""" Create a complete test data fixture for e2e tests of various clients """

from autofixture import AutoFixture, generators
from postcards.models import Postcard
from django.contrib.auth.models import User


def create(user_name, count=30):
    count = int(count)

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

    print(user_name)
    user = User.objects.get(username=user_name)

    postcard_fixture = AutoFixture(
        Postcard,
        field_values={
            'cover': generators.ChoicesGenerator(values=cover_files),
            'receiver': user
        }
    )

    clean()

    postcard_fixture.create(count)


def clean():
    Postcard.objects.all().delete()
