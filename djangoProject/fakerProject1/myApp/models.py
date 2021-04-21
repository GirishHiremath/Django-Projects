from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    num=models.IntegerField()
    marks=models.IntegerField()
    email=models.EmailField()
    ph=models.IntegerField()
