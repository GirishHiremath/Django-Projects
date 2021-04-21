from django.shortcuts import render
from myApp.models import Student
from math import sqrt
def student_view(request):
    s=Student.objects.all()
    print(type(s))
    d={'student':s}
    return render(request,'myApp/1.html',d)
