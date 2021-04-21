from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eexp=models.FloatField()
