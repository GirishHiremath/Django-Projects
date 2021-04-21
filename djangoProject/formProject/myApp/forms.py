from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    num=forms.IntegerField()
    marks=forms.FloatField()
