from django.conf.urls import patterns, url, include
from rest_framework import routers
from rucs.views import RucViewSet

router = routers.DefaultRouter()
router.register(r'ruc', RucViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
) 
