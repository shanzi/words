from django.contrib import admin
from words.keywords.models import *


admin.site.register(Keyword)
admin.site.register(KeywordPost)
admin.site.register(KeywordSection)
