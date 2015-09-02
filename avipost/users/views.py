from django.http import HttpResponse
from social.apps.django_app.utils import psa
from .tools import get_access_token

@psa('social:complete')
def register_by_access_token(request, backend):

    token = request.GET.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        return get_access_token(user)
    else:
        return HttpResponse("error")
