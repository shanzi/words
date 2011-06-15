from django.shortcuts import render_to_response
from django.http import HttpResponse

from words.keywords.forms import *
from django.contrib.auth.models import User

def add(request):
    owner=User.objects.all()[0]
    user_name="%s %s" % (owner.first_name,owner.last_name)
    if request.user.is_authenticated():
        authed=True
    if request.POST:
        form=KeywordsFrom(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['keywords'])
    else:
        form=KeywordsFrom()
    form['section'].field.choices=[ (x,x) for x in owner.sections.all()]
    return render_to_response('add_keywords.html',locals())


