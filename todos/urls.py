from django.conf.urls.defaults import patterns, include, url
from words.todos.views import *

urlpatterns= patterns('',
        url(r'^$',index),
        url(r'^new$',new),
        url(r'^list$',todolist),
        url(r'^done/(\d+)$',done),
        url(r'^undone/(\d+)$',undone),
        url(r'^highlight/(\d+)$',highlight),
        url(r'^unhighlight/(\d+)$',unhighlight), 
        url(r'^login/$',login),
        )
