from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    eexp=models.IntegerField()
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=100)
    eph=models.IntegerField()
    def __str__(self):
        return self.ename
