from django.shortcuts import render_to_response,get_object_or_404
from words.pictures.models import Picture
from words.pictures.forms import PictureUpload
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

@login_required
def index(request):
    return direct_to_template(request,'pictures/index.html')

def picture(request,id):
    image=get_object_or_404(Picture,id=id)
    homepage=image.user.profile.homepage
    moreimages=image.user.pictures.order_by('?')[:10]
    if(len(moreimages)<2):
        moreimages=None
    return render_to_response('pictures/picture.html',locals())


@login_required
def upload(request):
    img=None;
    if request.POST:
        form=PictureUpload(request.POST,request.FILES,request.user)
        img=form.save()
    return render_to_response('pictures/upload.html',{'image':img})

