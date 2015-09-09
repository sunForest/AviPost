from autofixture import AutoFixture
from django.utils.timezone import now, timedelta

test_user_name = settings.TEST_CONFIG['USER_NAME'] # noqa
test_token = settings.TEST_CONFIG['TOKEN'] # noqa

user_fixture = AutoFixture(
    User,  # noqa
    field_values={
        'username': test_user_name,
        'is_staff': False,
    }
)

User.objects.filter(is_staff=False).delete() # noqa
user = user_fixture.create(1)[0]

token_fixture = AutoFixture(
    AccessToken, # noqa
    field_values={
        'user': user,
        'scope': 'read write',
        'expires': now() + timedelta(seconds=10000000),
        'token': test_token
    })

token_fixture.create(1)
