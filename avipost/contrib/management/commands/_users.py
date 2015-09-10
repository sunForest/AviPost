from autofixture import AutoFixture
from django.utils.timezone import now, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken


def create():
    test_user_name = settings.TEST_CONFIG['USER_NAME']
    test_token = settings.TEST_CONFIG['TOKEN']

    user_fixture = AutoFixture(
        User,  # noqa
        field_values={
            'username': test_user_name,
            'is_staff': False,
        }
    )

    clean()

    user = user_fixture.create(1)[0]

    token_fixture = AutoFixture(
        AccessToken,
        field_values={
            'user': user,
            'scope': 'read write',
            'expires': now() + timedelta(seconds=10000000),
            'token': test_token
        })

    # currently only support generating one user per time
    token_fixture.create(1)


def clean():
    User.objects.filter(is_staff=False).delete()
