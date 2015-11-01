from autofixture import AutoFixture
from postcards.models import Messenger


def create():

    messengers = [('European Goldfinch', 'messengers/european_goldfinch.png'),
                  ('European Robin', 'messengers/european_robin.png')]

    clean()

    for name, portrait in messengers:
        AutoFixture(
            Messenger,
            field_values={
                'portrait': portrait,
                'name': name
            }
        ).create()


def clean():
    Messenger.objects.all().delete()
