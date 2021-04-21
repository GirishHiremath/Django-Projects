from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class student_list_view(ListView):
    model=Student
    #dfl template:student_list.html
    #dfl context:student_list


class student_detail_view(DetailView):
    model=Student
    #dfl template:student_detail.html
    #dfl context:student
class student_create_view(CreateView):
    model=Student
    fields="__all__"
    #dfl template:student_form.html
class student_update_view(UpdateView):
      model=Student
      fields=('name','marks','place')
      #dfl template:student_form.html
class student_delete_view(DeleteView):
    model=Student
    success_url=reverse_lazy("home")

def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=post.objects.filter(title__icontains=q)
    else:
        #posts=post.objects.all()
        raise Exception("Record not found")
    return render(request,'myApp/display.html')
