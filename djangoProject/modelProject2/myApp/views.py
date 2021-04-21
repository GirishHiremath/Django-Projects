from django.shortcuts import render
from myApp.models import Employee

def emp_view(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'myApp/1.html',d)
