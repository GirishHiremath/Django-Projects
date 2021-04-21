from django.shortcuts import render
from myApp.models import Student


def Student_view(request):
    s=Student.objects.all().order_by("-marks")[0:10]
    d={'stud':s}
    return render(request,'myApp/1.html',d)
