from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['name','num','marks','place']
admin.site.register(Student,StudentAdmin)
