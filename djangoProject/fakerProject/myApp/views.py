from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def view1(r):
    s=Student.objects.all()
    d={'s':s}
    return render(r,'myApp/1.html',d)
