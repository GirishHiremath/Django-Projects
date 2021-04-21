from django import forms
from myApp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        exclude=['esal','eexp']
