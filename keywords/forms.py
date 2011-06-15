import django.forms as forms
from words.keywords.models import KeywordSection

class KeywordsFrom(forms.Form):
    section=forms.ChoiceField()
    keywords=forms.CharField()

