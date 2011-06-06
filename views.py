from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def index(request):
    """docstring for index"""
    user=User.objects.all()[0]
    info_pairs=user.contact_info_pairs.order_by('pair_order').all()
    return render_to_response('index.html',locals())

