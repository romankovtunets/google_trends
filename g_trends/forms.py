from django import forms

class KeyWords(forms.Form):
    keywords = forms.CharField(label="Keywords", max_length=256)
