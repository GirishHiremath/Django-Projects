import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerProject.settings')
import django
django.setup()
from faker import Faker
from myApp.models import Student
from random import randint
f=Faker()
def get_ph():
    d1=randint(6,9)
    x=str(d1)
    for i in range(9):
        x=x+str(randint(0,9))
    return x
def populate(n):
    for i in range(n):
          fname=f.name()
          fnum=f.random_int(1,10)
          fdob=f.date_of_birth()
          femail=f.email()
          fmarks=f.random_int(1,100)
          fph=get_ph()
          s=Student.objects.get_or_create(name=fname,num=fnum,dob=fdob,email=femail,marks=fmarks,ph=fph)
populate(10)
