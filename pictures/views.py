from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse
from words.pictures.models import Picture
from words.pictures.forms import PictureUpload
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render_to_response('pictures/index.html')

def picture(request,id):
    image=get_object_or_404(Picture,id=id)
    if request.user.is_authenticated() and request.user == image.user:
        editable=True
    else:
        editable=False
    if request.POST and editable:
        if request.POST.has_key('title'):
            image.title=request.POST['title']
        if request.POST.has_key('detail'):
            image.detail=request.POST['detail']
        image.save()
        return HttpResponse('(["%s","%s"])' % (image.title,image.detail))
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

