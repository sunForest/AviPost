from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from rest_framework import routers
from postcards.views import PostcardViewSet

router = routers.DefaultRouter()
router.register(r'postcards', PostcardViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)

if settings.DEBUG:
    import autofixture
    autofixture.autodiscover()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
