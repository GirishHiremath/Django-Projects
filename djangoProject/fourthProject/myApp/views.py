from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    s="<h1>First response</h1>"
    return HttpResponse(s)

def view2(request):
    s="<h1>second response</h1>"
    return HttpResponse(s)
