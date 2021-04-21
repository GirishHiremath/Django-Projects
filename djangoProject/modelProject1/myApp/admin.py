from django.contrib import admin
from myApp.models import Student
class StudentAdmin(admin.ModelAdmin):
    l=['name','num','marks']

admin.site.register(Student,StudentAdmin)
