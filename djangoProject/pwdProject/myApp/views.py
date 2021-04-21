from django.shortcuts import render
from myApp.forms import SignUpForm

def view1(request):
    s=SignUpForm()
    d={'f':s}
    if request.method=='POST':
        s=SignUpForm(request.POST)
        if(s.is_valid()):
            name=s.cleaned_data['name']
            pwd=s.cleaned_data['pwd']
            rpwd=s.cleaned_data['rpwd']
            email=s.cleaned_data['email']
            d={'name':name,'pwd':pwd,'rpwd':rpwd,'email':email}
            return render(request,'myApp/output.html',d)
    return render(request,'myApp/input.html',d)
