from django.http import HttpResponse
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from .tools import get_access_token
#from .models import OAuthUser

@psa('social:complete')
def register_by_access_token(request, backend):

    token = request.GET.get('access_token')
    user = request.backend.do_auth(token)

    if user:
        # try:
        #     localUser = OAuthUser.objects.get(username=user, provider=backend)
        # except OAuthUser.DoesNotExist:
        #
        #     localUser = OAuthUser.objects.create(username=user, provider=backend, email=user.email)
        # login(request, user)
        return get_access_token(user)
    else:
        return HttpResponse("error")
