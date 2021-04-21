from django.shortcuts import render,redirect


# Create your views here.
from django.contrib.auth.decorators import login_required
from myApp.forms import myForm

def home_view(request):
    return render(request,'myApp/home.html')

@login_required
def java_view(request):
    return render(request,'myApp/java.html')

@login_required
def python_view(request):
    return render(request,'myApp/python.html')

@login_required
def apti_view(request):
    return render(request,'myApp/apti.html')

def logout_view(request):
    return render(request,'myApp/logout.html')

def signup_view(request):
    f=myForm()
    if request.method=="POST":
        f=myForm(request.POST)
        if f.is_valid():
            user=f.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    return render(request,'myApp/signup.html',{'form':f})
