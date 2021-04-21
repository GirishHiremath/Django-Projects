from django import forms

from django.core.exceptions import ValidationError
from django.core import validators
def my_fun(data):
    if data[0].lower()!='s':
        raise Exception("Name should start with s")
class FeedBack(forms.Form):
    name=forms.CharField(validators=[my_fun])
    rollno=forms.IntegerField()
    email=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea)
