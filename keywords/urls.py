from django.conf.urls.defaults import patterns, include, url
from words.keywords.views import *

urlpatterns=patterns('',
        url(r'^add/',add),
        )
