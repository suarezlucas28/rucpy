from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    ##==============APP RUCS================
    url(r'^rucs/', include("rucs.urls", namespace="rucs")),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^admin/', include(admin.site.urls)),
]
