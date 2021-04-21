from django.contrib import admin
from myApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    l=['name','num','marks','email','ph']
admin.site.register(Student,StudentAdmin)
