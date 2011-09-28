from django.db import models
from django.contrib.auth.models import User

class Keyword(models.Model):
    """docstring"""
    title = models.CharField(max_length=16)
    def __unicode__(self):
        return self.title

class Log(models.Model):
    """docstring"""
    title = models.CharField(max_length=64)
    abstract = models.CharField(max_length=256, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='logs')
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    shorturl = models.URLField(verify_exists=False, max_length=200, blank=True)
    keywords = models.ManyToManyField(Keyword, related_name='logs')
    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
        return (self.shorturl )


class Comment(models.Model):
    """docstring"""
    Log = models.ForeignKey(Log, related_name='comments')
    content = models.CharField(max_length=256)
    commenter_name = models.CharField(max_length=64)
    commenter_email = models.EmailField(max_length=64)
    def __unicode__(self):
        return "comment: %s" % commenter_name

