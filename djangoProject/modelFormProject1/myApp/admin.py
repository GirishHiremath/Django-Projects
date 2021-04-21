from django.contrib import admin

from myApp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    l=['eno','ename','esal','eexp']
admin.site.register(Employee,EmployeeAdmin)
