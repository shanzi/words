from django.shortcuts import render_to_response,get_object_or_404
from words.pictures.models import Picture
from words.pictures.forms import PictureUpload
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated():
        authed=True
        user=request.user
    else:
        authed=False
    return render_to_response('pictures/index.html',locals())

def picture(request,id):
    image=get_object_or_404(Picture,id=id)
    return render_to_response('pictures/picture.html',locals())


@login_required
def upload(request):
    img=None;
    if request.POST:
        form=PictureUpload(request.POST,request.FILES,request.user)
        img=form.save()
    return render_to_response('pictures/upload.html',{'image':img})

