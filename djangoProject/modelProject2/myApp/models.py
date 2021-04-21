from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.model import PhoneNumberField
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    eage=models.IntegerField()
    eexp=models.IntegerField()
    esal=models.FloatField()
    edob=models.DateField()
    eplace=models.CharField(max_length=40)
    eph=PhoneNumberField(null=False, blank=False, unique=True)
    eemail=models.EmailField()
    def __str__(self):
        return self.eid
