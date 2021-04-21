from django.shortcuts import render
from myApp.models import Bank


# Create your views here.
def display(request):
    b=Bank.objects.all()
    d={'bank':b}
    return render(request,'myApp/bank_list.html',d)

def detail_view(request,id):
    b=Bank.objects.get(id=id)
    d={'b':b}
    return render(request,'myApp/bank_detail.html',d)
