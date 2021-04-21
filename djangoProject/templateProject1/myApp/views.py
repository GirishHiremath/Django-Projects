from django.shortcuts import render
import datetime
def view1(request):
    dt=datetime.datetime.now()
    h=int(dt.strftime('%H'))
    if h<12:
        msg="good morning"
    elif h<16:
        msg="good afternoon"
    elif h<21:
        msg="good evening"
    else:
        msg="good night"
    d={'message':msg,'dt1':dt}
    return render(request,'myApp/1.html',d)
    
