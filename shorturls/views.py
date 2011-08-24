# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from words.shorturls.models import *
from django.shortcuts import get_object_or_404
import re

def make_shorturl(n):
    """docstring for make_shorturl"""
    dic="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM_"
    shorturl=''
    while(n>0):
        shorturl+=dic[n%len(dic)]
        n=int(n/len(dic))
    return shorturl

def expand_shorturl(request,url=""):
    """docstring for index"""
    shorturl=get_object_or_404(ShortUrl,url=url)
    return HttpResponseRedirect(shorturl.origin) 

def new_shorturl(request):
    """docstring for add"""
    if request.POST.has_key('url'):
        url=request.POST['url']
    elif request.GET.has_key('url'):
        url=request.GET['url']
    else:
        return HttpResponseBadRequest()
    if not re.match(r'^(\w|\d)+://',url):
        url='http://'+url
    if len(url)<10:
        return HttpResponse("({'origin':'%s','shorturl':'%s'})" % (url,url))
    (shorturl,is_create)=ShortUrl.objects.get_or_create(origin=url)
    if is_create:
        shorturl.url=make_shorturl(shorturl.id)
        shorturl.save()
    return HttpResponse("({'origin':'%s','shorturl':'%s'})" % (url,str(shorturl)))
