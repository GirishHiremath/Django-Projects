from django import forms
class Student(forms.Form):
    name=forms.CharField()
    num=forms.IntegerField()
    marks=forms.FloatField()
