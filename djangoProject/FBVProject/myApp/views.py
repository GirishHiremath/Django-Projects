from django.shortcuts import render,redirect
from myApp.models import Employee
from myApp.forms import EmployeeForm
from django.http import HttpResponse
# Create your views here.
def display(request):
    e=Employee.objects.all()
    d={'e':e}
    return render(request,'myApp/index.html',d)

    '''if 'q' in request.GET:
        q=request.GET['q']
        posts=post.objects.filter(title__icontains=q)
    else:
        posts=post.objects.all()
        raise Exception("Record not found")
    return render(request,'myApp/display.html')'''

def insert_view(request):
    f=EmployeeForm()
    if request.method=="POST":
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/home')
    d={'f':f}
    return render(request,'myApp/insert.html',d)

def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('/home')
    #return HttpResponse("Successfully deleted")

def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=="POST":
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
           f.save(commit=True)
        return redirect("/home")
    return render(request,'myApp/update.html',{'e':e})

def search(request,id):
    e=Employee.objects.get(id=id)
    d={'e':e}
    return render(request,'myApp/display.html',d)

    '''if 'q' in request.GET:
        q=request.GET['q']
        posts=post.objects.filter(title__icontains=q)'''
    '''e=Employee.objects.filter('esal')
    d={'e':e}
    return render(request,'myApp/display.html',d)'''
