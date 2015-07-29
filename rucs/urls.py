from django.conf.urls import patterns, url, include
from rucs.views import ruc_detail



urlpatterns = patterns('',
   url(r'^ruc/(?P<ci>\d+)/$', ruc_detail, name='detail'),
) 
