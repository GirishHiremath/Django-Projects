from django.contrib import admin
from myApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    l=['eid','ename','eage','eexp','esal','edob','eplace','eph','eemail']

admin.site.register(Employee,EmployeeAdmin)
