# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    """docstring for index"""
    return render_to_response("diumoo/index.html")
