# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from words.shorturls.models import *
from django.shortcuts import get_object_or_404,render_to_response
from django.contrib.auth.decorators import login_required
from django.conf import settings
import re,httplib

def gen_shorturl(n):
    """docstring for make_shorturl"""
    dic="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM_"
    shorturl=''
    while(n>0):
        shorturl+=dic[n%len(dic)]
        n=int(n/len(dic))
    return shorturl

def make_shorturl(url):
    (shorturl,is_create)=ShortUrl.objects.get_or_create(origin=url)
    if is_create:
        shorturl.url=gen_shorturl(shorturl.id)
        shorturl.save()
    return str(shorturl)

def expand_shorturl(shorturl,url):
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
    if not re.match(r'^[\w\d]+://',url):
        url='http://'+url
    if len(url)<10:
        return HttpResponse("({'origin':'%s','shorturl':'%s'})" % (url,url))
    return HttpResponse("({'origin':'%s','shorturl':'http://%s'})" % (url,make_shorturl(url)))

def shorturl_index(request):
    if request.POST.has_key('url'):
        url=re.sub(r'^(http|https|ftp)://','',request.POST['url'])
    else:
        return render_to_response('shorturl.html',{'short_url_root':settings.SHORT_URL_ROOT})
    g=re.match('(is\.gd|bit\.ly|t\.co|isnot\.tk|goo\.gl)/([\w\d_]+)',url)
    if g:
        (domin,sub)=g.groups()
        if(domin.lower()=='isnot.tk'):
            shorturl=get_object_or_404(ShortUrl,url=sub)
            return HttpResponse("({'longurl':'%s'})"% shorturl.origin)
        else:
            con=httplib.HTTPConnection(domin,timeout=5)
            try:
                con.request('GET',('/%s'% sub))
            except:
                return HttpResponseBadRequest()
            result=con.getresponse()
            if result.status in [301,302]:
                location=result.getheader('location')
                return HttpResponse("({'longurl':'%s'})" % location)
    else:
        if re.match(r'^([\w\d\-]+\.)+(\w+)(\/\S*)?$',url):
            return new_shorturl(request)

    return HttpResponseBadRequest()
