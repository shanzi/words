import django.forms as forms
from words.pictures.models import Picture
from django.conf import settings
from datetime import datetime
import ImageFile
import Image
import os


def save_image(size,dt,image):
    if not os.path.isdir(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
    size_path=os.path.join(settings.MEDIA_ROOT,size)
    if not os.path.isdir(size_path):
        os.mkdir(size_path)
    date_path=os.path.join(size_path,dt.strftime('%Y%m'))
    if not os.path.isdir(date_path):
        os.mkdir(date_path)
    image.save(os.path.join(date_path,'%s.jpg' % dt.strftime('%d%H%M')),'JPEG')
    return "/media/%s/%s/%s.jpg" % (size,dt.strftime('%Y%m'),dt.strftime('%d%H%M'))


class PictureModify(forms.Form):
    title=forms.CharField(max_length=64)
    detail=forms.CharField(max_length=512,required=False)

class PictureUpload(forms.Form):
    image = forms.ImageField()
    def __init__(self,data=None,file_data=None,user=None):
        self.data=data
        self.file_data=file_data
        self.user=user
        if not (data and file_data):
            forms.Form.__init__(self)
        else:
            forms.Form.__init__(self,data,file_data)
    def save(self):
        if forms.Form.is_valid(self) and self.user.is_authenticated():
            f=self.file_data['image']
            parser=ImageFile.Parser()
            for chunk in f.chunks():
                parser.feed(chunk)
            img=parser.close()
            if not img.mode=="RGB":
                img=img.convert("RGB")
            pic=Picture()
            pic.user=self.user
            dt=datetime.now()
            (pic.width,pic.height)=img.size
            pic.fullsize=save_image('fullsize',dt,img)
            img.thumbnail((600,600),Image.ANTIALIAS)
            pic.medium=save_image('medium',dt,img)
            img.thumbnail((100,100),Image.ANTIALIAS)
            pic.thumbnail=save_image('thumbnail',dt,img)
            pic.title=f.name
            return pic.save()
        return None




