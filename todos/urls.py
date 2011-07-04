from django.conf.urls.defaults import patterns, include, url
from words.todos.views import *

urlpatterns= patterns('',
        url(r'^$',index),
        url(r'^new$',new),
        url(r'^list$',todolist),
        )
