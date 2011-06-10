import django.forms as forms

class AuthedKeywordsForm(forms.Form):
    section = forms.ChoiceField()
    keywords = forms.CharField()

class KeywordsFrom(forms.Form):
    email = forms.EmailField()
    keywords = forms.CharField()

