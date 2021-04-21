from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    num=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    marks=models.IntegerField()
    ph=models.CharField(max_length=10)
    def __str__(self):
        return self.name
