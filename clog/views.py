# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect


def index(request):
    """docstring for index"""
    return render_to_response('clog/index.html',{'title':settings.CLOG_TITLE})

def search(request):
    """docstring for search"""
    return HttpResponseRedirect('http://www.google.com/#q=%s+site:ant.isnot.tk&oq=%s+site:ant.isnot.tk' % (request.GET['q'],request.GET['q']))

