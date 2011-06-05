from django.db import models
import re

# Create your models here.


class Keyword(models.Model):
	"""docstring"""
	name = models.CharField(max_length=75)
	permalink = models.CharField(max_length=75, blank=True)
	
	def __unicode__(self):
		return self.name
		
	
	def save(self, force_insert=False, force_update=False):
		s=re.sub(r'[^a-zA-Z_]+','_',self.name)
		s=re.sub(r'(^_)|(_$)','',s)
		if len(s)>=3:
			try:
				plink=Keyword.objects.get(permalink=s)
			except:
				self.permalink=s
		models.Model.save(self,force_insert,force_update)
	
	@models.permalink
	def get_absolute_url(self):
		if self.permalink:
			return '/keyword/%s/' % self.permalink
		else:
			return '/Keyword/%d/' % self.id
class KeywordPost(models.Model):

	"""docstring"""
	keyword = models.ForeignKey(Keyword, related_name='keyword_posts')
	email = models.EmailField(max_length=75, blank=True)
	def __unicode__(self):
		return self.email
		
	
	def create_post(name,email=None):
		kw,create = Keyword.objects.get_or_create(name=name)
		kp=KeywordPost()
		kp.keyword=kw
		kp.email=email
		kp.save()
		
	
	@models.permalink
	def get_absolute_url(self):
		return self.keyword.permalink()
