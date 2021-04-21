from django.shortcuts import render
from django.http import HttpResponse
import datetime
def view1(request):
    n1=int(input("enter 1st number:"))
    n2=int(input("enter 2nd number:"))
    n3=n1+n2
    s="sum="+str(n3)
    return HttpResponse(s)

def view2(request):
    dt=datetime.datetime.now()
    s="greetings of the day"+str(dt)
    return HttpResponse(s)
