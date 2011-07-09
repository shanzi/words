from django.conf.urls.defaults import patterns, url
from words.pictures.views import *



urlpatterns = patterns('',
        url(r'^$',index),
        url(r'^(\d+)$',picture),
        url(r'^upload$',upload),
        )
