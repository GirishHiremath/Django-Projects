from django.shortcuts import render
from myApp.models import Student
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class view1(ListView):
    model=Student
class view2(DetailView):
    model=Student
class view3(CreateView):
    model=Student
    fields='__all__'
class view4(UpdateView):
    model=Student
    fields=('name','marks')
class view5(DeleteView):
    model=Student
    success_url=reverse_lazy('response1')
