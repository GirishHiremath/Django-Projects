from django.contrib import admin
from myApp.models import Bank

class BankAdmin(admin.ModelAdmin):
    l=['name','branch','location','ifse','noOfCustomers','turnOver']
admin.site.register(Bank,BankAdmin)

# Register your models here.
