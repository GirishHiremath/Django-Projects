from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['name','num','dob','email','marks','ph']
admin.site.register(Student,StudentAdmin)
