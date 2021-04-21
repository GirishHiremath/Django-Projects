import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FBVProject.settings')
import django
django.setup()
from faker import Faker
from random import randint
from myApp.models import Employee
f=Faker()
def gen_ph():
    d1=randint(6,9)
    x=str(d1)
    for i in range(9):
        x=x+str(randint(0,9))
    return int(x)

def populate(n):
    for i in range(n):
        fno=f.random_int(1,30)
        fname=f.name()
        fexp=f.random_int(1,5)
        fsal=f.random_int(15000,100000)
        faddr=f.address()
        fph=gen_ph()
        e=Employee.objects.get_or_create(eno=fno,ename=fname,eexp=fexp,esal=fsal,eaddr=faddr,eph=fph)

populate(30)
        
