from django.shortcuts import render
from myApp.forms import FeedBack

def view1(request):
    f=FeedBack()
    d={'form':f}
    if request.method=='POST':
        f=FeedBack(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            rollno=f.cleaned_data['rollno']
            email=f.cleaned_data['email']
            comments=f.cleaned_data['comments']
            d={'name':name,'rollno':rollno,'email':email,'comments':comments}
            return render(request,'myApp/output.html',d)
    return render(request,'myApp/input.html',d)
