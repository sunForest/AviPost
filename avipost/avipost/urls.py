from django.conf.urls import patterns, include, url
#from django.contrib import admin
from rest_framework import routers
from postcards.views import PostcardViewSet



router = routers.DefaultRouter()
router.register(r'postcards', PostcardViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(router.urls)),

    #url(r'^admin/', include(admin.site.urls)),
)
