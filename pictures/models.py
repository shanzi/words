from django.db import models
from django.contrib.auth.models import User
import re,os
from django.conf import settings
# Create your models here.
class Picture(models.Model):
    user = models.ForeignKey(User, related_name='pictures')
    medium = models.ImageField(upload_to="/media/medium/")
    thumbnail = models.ImageField(upload_to="/media/thumbnail/")
    fullsize = models.ImageField(upload_to="/media/fullsize/")
    title = models.CharField(max_length=64)
    detail = models.CharField(max_length=512, blank=True)
    permalink = models.CharField(max_length=64, blank=True)
    
    def __unicode__(self):
        return self.title
    def save(self):
        if self.permalink:
            return models.Model.save(self)
        p=re.sub(r'(\W|_)+','_',self.title)
        p=re.sub(r'(^_+)|(_+$)','',p)
        if len(p)>1:
            self.permalink=p
        models.Model.save(self)
    @models.permalink
    def get_absolute_url(self):
        if self.permalink:
            return "/pic/%s/" % self.permalink
        else:
            return "/pic/%d/" % self.id
    def delete(self):
        try:
            os.remove("%s/words%s" % (settings.HERE,str(self.fullsize)))
            os.remove("%s/words%s" % (settings.HERE,str(self.medium)))
            os.remove("%s/words%s" % (settings.HERE,str(self.thumbnail)))
        except:
            pass
        return models.Model.delete(self)

class Comment(models.Model):
    """docstring"""
    email = models.EmailField(max_length=75)
    nickname = models.CharField(max_length=75)
    content = models.CharField(max_length=200)
    picture = models.ForeignKey(Picture, related_name='comments')
    def __unicode__(self):
       return self.content
