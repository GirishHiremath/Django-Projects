from django.shortcuts import render
from myApp.forms import StudentForm
from myApp.models import Student
# Create your views here.
def view1(request):
    f=StudentForm()
    d={'f':f}
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
    return render(request,'myApp/input.html',d)
def view2(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myApp/output.html',d)
    
