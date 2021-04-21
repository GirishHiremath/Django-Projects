from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def java_test_view(request):
    return render(request,'myApp/javatest.html')
def logout_view(request):
    return render(request,'myApp/logout.html')
    
