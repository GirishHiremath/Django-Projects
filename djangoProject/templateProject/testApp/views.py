from django.shortcuts import render
import datetime

def employee_view(request):
    dt=datetime.datetime.now()
    name="Ramu"
    exp=4
    salary=80000
    place="Hyderabad"
    d={"datetime":dt,"ename":name,"eexp":exp,"esal":salary,"eplace":place}
    return render(request,'testApp/1.html',d)
