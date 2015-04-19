from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from rest_framework import routers

from postcards.views import PostcardViewSet



router = routers.DefaultRouter()
router.register(r'postcards', PostcardViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(router.urls)),

    #url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT);
