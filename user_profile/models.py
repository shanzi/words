from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	"""docstring"""
	user = models.OneToOneField(User,  related_name='profile')
	profile = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.profile

class ContactInfoPair(models.Model):
	"""docstring"""
	user = models.ForeignKey(User, related_name='contact_info_pairs')
	pair_order = models.IntegerField()
	type = models.CharField(max_length=16, blank=True)
	key = models.CharField(max_length=75)
	value = models.CharField(max_length=75)
	def __unicode__(self):
		return "%s : %s" % self.key, self.value

	def save(self, force_insert=False, force_update=False):
		if not self.type:
			self.type='text'
		if not self.pair_order:
			self.pair_order=0
		return models.Model.save(self)

