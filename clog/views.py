# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings

def index(request):
    """docstring for index"""
    return render_to_response('clog/index.html',{'title':settings.CLOG_TITLE})

