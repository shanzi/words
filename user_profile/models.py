from django.db import models
from django.contrib.auth.models import User
import hashlib
# Create your models here.

class UserProfile(models.Model):
	"""docstring"""
	user = models.OneToOneField(User,  related_name='profile')
        title = models.CharField(max_length=75,default='Title')
        sub_header = models.CharField(max_length=60, blank=True)
	profile = models.CharField(max_length=256, blank=True)
        gravatar_img= models.CharField(max_length=200, blank=True)

	def __unicode__(self):
		return self.title

        def save(self):
            """docstring for save"""
            self.gravatar_img="http://www.gravatar.com/avatar/" + hashlib.md5(self.user.email.lower()).hexdigest()+'.jpg?s=60'
            models.Model.save(self)

class ContactInfoPair(models.Model):
	"""docstring"""
	user = models.ForeignKey(User, related_name='contact_info_pairs')
	pair_order = models.IntegerField()
	type = models.CharField(max_length=16, blank=True)
	key = models.CharField(max_length=75)
	value = models.CharField(max_length=75)
	def __unicode__(self):
		return "%s : %s" % (self.key, self.value)

	def save(self, force_insert=False, force_update=False):
		if not self.type:
			self.type='text'
		if not self.pair_order:
			self.pair_order=0
		return models.Model.save(self)

