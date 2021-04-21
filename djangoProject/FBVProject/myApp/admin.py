from django.contrib import admin
from myApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    l=['eno','ename','eexp','esal','eaddr','eph']
admin.site.register(Employee,EmployeeAdmin)
