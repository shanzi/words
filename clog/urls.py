from django.conf.urls.defaults import patterns, url
from words.clog.views import *



urlpatterns = patterns('',
        url(r'^$',index),
        )
