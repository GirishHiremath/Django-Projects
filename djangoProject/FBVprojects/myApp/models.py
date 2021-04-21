from django.db import models
class Bank(models.Model):
    name=models.CharField(max_length=40)
    branch=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    ifse=models.CharField(max_length=30)
    noOfCustomers=models.IntegerField()
    turnOver=models.IntegerField()

# Create your models here.
