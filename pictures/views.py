from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from words.pictures.models import Picture
from words.pictures.forms import PictureUpload
from django.contrib.auth.decorators import login_required
from words.twitter.views import update as twitter_update

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

@login_required
def delete(request,id=""):
    if request.POST and request.POST.has_key('confirm_target'):
        pic=get_object_or_404(Picture,id=int(request.POST['confirm_target']))
        if pic.user.id!= request.user.id:
            return HttpResponseForbidden();
        else:
            detail='The picture \"%s\" has been sucessfully deleted!' % pic.title
            pic.delete()
            return render_to_response('success.html',{'title':'Delete Picture Success','detail':detail})
    else:
        pic=get_object_or_404(Picture,id=int(id))
        request.session['operation_title']='DELETE %s' % pic.title        
        request.session['operation_detail']='Are your sure to DELETE picture "%s"?' % pic.title
        request.session['operation_callback']="/pictures/delete/"
        request.session['operation_target']=pic.id
        request.session['operation_snap']="<img src='%s' />" % pic.medium
        return HttpResponseRedirect('/confirm/') 

@login_required
def tweet(request,id):
    pic=get_object_or_404(Picture,id=id)
    if pic.user.id != request.user.id:
        return HttpResponseForbidden()
    else:
        status="(Photo:http://%s) %s" % (pic.shorturl,pic.title,pic.detail)
        return twitter_update(request,"Tweet a photo!",status)

