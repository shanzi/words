from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from words.views import *
from words.shorturls.views import expand_shorturl,new_shorturl,shorturl_index
from django.contrib.auth.views import login,logout




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'words.views.home', name='home'),
        url(r'^pictures/', include('words.pictures.urls')),
        url(r'^todos/',include('words.todos.urls')),
        url(r'^confirm/?',confirm),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^$',index),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^keywords/',include('words.keywords.urls')),
        url(r'^twitter/',include('words.twitter.urls')),
        url(r'^shorturl/$',shorturl_index),
        url(r'^shorturl/new/$',new_shorturl),
        url(r'^accounts/login/$',login,{'template_name':'login.html'}),
        url(r'^([a-zA-z0-9_]{1,5})$',expand_shorturl),
        )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
