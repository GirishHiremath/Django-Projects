from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    msg="<h1>Response through 1st application</h1>"
    return HttpResponse(msg)
