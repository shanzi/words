from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    user = models.ForeignKey(User, related_name='todos')
    name = models.CharField(max_length=140)
    detail = models.CharField(max_length=512, blank=True)
    highlight = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    def __unicode__(self):
       return self.user
    
    @models.permalink
    def get_absolute_url(self):
        return ('/todos/detail/%d' % self.id )

