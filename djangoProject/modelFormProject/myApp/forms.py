from django import forms
from myApp.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['name']
