import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerProject1.settings')
import django
django.setup()
from faker import Faker
from myApp.models import Student
from random import randint
f=Faker()

def gen_phno():
    d1=randint(6,9)
    x=str(d1)
    for i in range(9):
        x=x+str(randint(0,9))
    return int(x)



def populate(n):
    for i in range(n):
        fname=f.name()
        fnum=f.random_int(1,100)
        fmarks=f.random_int(1,100)
        femail=f.email()
        fph=gen_phno()
        s=Student.objects.get_or_create(name=fname,num=fnum,marks=fmarks,email=femail,ph=fph)
populate(25)
