from django import forms

class WordCountForm(forms.Form):
    file = forms.FileField()
    word = forms.CharField(max_length=100)
