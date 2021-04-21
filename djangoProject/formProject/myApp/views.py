from django.shortcuts import render
from myApp.forms import StudentForm

def view1(request):
    s=StudentForm()
    d={'f':s}
    if request.method=='POST':
       s=StudentForm(request.POST)
       if s.is_valid():
           name=s.cleaned_data['name']
	       num=s.cleaned_data['num']
	       marks=s.cleaned_data['marks']
	       d={'name':name,'num':num,'marks':marks}
	       return render(request,'myApp/output.html',d)
    return render(request,'myApp/input.html',d)
