from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import hashlib


def get_gravatar(email):
    return "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()+'.jpg?s=60'

def index(request):
    """docstring for index"""
    user=User.objects.all()[0]
    info_pairs=user.contact_info_pairs.order_by('pair_order').all()
    if user.first_name and user.last_name:
        name= "%s %s" % (user.first_name,user.last_name)
    else:
        name=user.username
    gravatar_img=get_gravatar(user.email)
    return render_to_response('index.html',locals())

