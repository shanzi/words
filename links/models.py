from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    """docstring"""
    user = models.ForeignKey(User, related_name='links')
    title = models.CharField(max_length=75)
    link = models.URLField(verify_exists=False, max_length=200)
    detail = models.CharField(max_length=140, blank=True)
    
    def __unicode__(self):
        return self.title
    
