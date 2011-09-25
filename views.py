from django.shortcuts import render_to_response
from django.http import HttpResponseForbidden,HttpResponseServerError
from django.contrib.auth.models import User
from keywords.models import Keyword
from django.contrib.auth.decorators import login_required

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

@login_required
def confirm(request):
    """docstring for confirm"""
    ss=request.session
    if ss.has_key('operation_snap'):
        snap=ss['operation_snap']
    else:
        snap=None
    try:
        if ss.has_key('operation_title') and ss.has_key('operation_detail') and ss.has_key('operation_target') and ss.has_key('operation_callback'):
            res=render_to_response('confirm.html',{'title':ss['operation_title'],'detail':ss['operation_detail'],'callback':ss['operation_callback'],'target':ss['operation_target'],'snap':snap})
        else:
            res=HttpResponseForbidden()
    except Exception,e:
        raise e
        return HttpResponseServerError()
    else:
        for key in ['operation_title','operation_detail','operation_target','operation_callback','operation_snap']:
            try:
                del ss[key]
            except:
                continue
    return res

