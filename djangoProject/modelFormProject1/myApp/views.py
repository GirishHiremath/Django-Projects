from django.shortcuts import render
from myApp.forms import EmployeeForm
from myApp.models import Employee
def view1(request):
    f=EmployeeForm()
    d={'f':f}
    if request.method=="POST":
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
    return render(request,'myApp/input.html',d)
def view2(request):
    e=Employee.objects.all().order_by('eno')
    d={'emp':e}
    return render(request,'myApp/output.html',d)   
