from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    ##==============APP RUCS================
    url(r'^rucs/', include("rucs.urls", namespace="rucs")),
    
    url(r'^admin/', include(admin.site.urls)),
]
