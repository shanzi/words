from django.db import models
from django.conf import settings


# Create your models here.
class ShortUrl(models.Model):
    """docstring"""
    url = models.CharField(max_length=200)
    origin = models.URLField(verify_exists=False, max_length=200)
    
    def __unicode__(self):
        return "%s/%s" % (settings.SHORT_URL_ROOT,self.url)
        
    
    @models.permalink
    def get_absolute_url(self):
        return self.origin

