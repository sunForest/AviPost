from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from rest_framework import routers
from postcards.views import PostcardViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'postcards', PostcardViewSet, 'Postcard')
router.register(r'users', UserViewSet, 'User')

urlpatterns = patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include(router.urls)),
    url(r'^authentication/', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
