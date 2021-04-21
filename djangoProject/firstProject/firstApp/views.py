from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    s="<h1>welcome to django</h1>"
    return HttpResponse(s)
