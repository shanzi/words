from django.shortcuts import render_to_response
from words.keywords.forms import *
from django.contrib.auth.models import User

def add(request):
    owner=User.objects.all()[0]
    user_name="%s %s" % (owner.first_name,owner.last_name)
    choices=[(0,'None')]
    authed=False
    i=1
    for section in owner.sections.all():
        choices.append((i,section.title))
        i=i+1
    if request.user.is_authenticated():
        Form=AuthedKeywordsForm
        authed=True
    else:
        Form=KeywordsFrom
    if request.POST:
        form=Form(request.POST,choices=choices)
        if form.is_valid():
            return render_to_response(form.cleaned_data['keywords'])
    form=Form()
    form['section'].field.choices=choices
    return render_to_response('add_keywords.html',locals())


