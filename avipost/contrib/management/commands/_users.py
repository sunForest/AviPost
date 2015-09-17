from autofixture import AutoFixture
from django.utils.timezone import now, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken


def create(user_name, token):
    user_fixture = AutoFixture(
        User,  # noqa
        field_values={
            'username': user_name,
            'is_staff': False,
        }
    )

    user = user_fixture.create(1)[0]
    print(user.id)

    token_fixture = AutoFixture(
        AccessToken,
        field_values={
            'user': user,
            'scope': 'read write',
            'expires': now() + timedelta(seconds=10000000),
            'token': token
        })

    # currently only support generating one user per time
    token_fixture.create(1)
