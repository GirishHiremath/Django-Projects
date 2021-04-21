from django.shortcuts import render


d={'n':"Dhoni",'p':"Blore"}
def view1(request):
    return render(request,'myApp/1.html',d)
