from django.shortcuts import render
from django.http import HttpResponse
def view2(request):
    msg="<h1>Response through 2nd application</h1>"
    return HttpResponse(msg)
