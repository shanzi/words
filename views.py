from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from keywords.models import Keyword



def index(request):
    """docstring for index"""
    user=User.objects.all()[0]
    info_pairs=user.contact_info_pairs.order_by('pair_order').all()
    if user.first_name and user.last_name:
        name= "%s %s" % (user.first_name,user.last_name)
    else:
        name=user.username
    gravatar_img=user.profile.gravatar_img
    other_keywords=Keyword.objects.filter(section=None).all()
    return render_to_response('index.html',locals())

