from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    """docstring"""
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, related_name='logs')
    content = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField( auto_now=True)

    permalink = models.URLField(verify_exists=False, max_length=200, blank=True)
    shorturl = models.URLField(verify_exists=False, max_length=200, blank=True)

    class Meta:
        
    
    def __unicode__(self):
        return self.title
        
    @models.permalink
    def get_absolute_url(self):
        return (self.permalink )

