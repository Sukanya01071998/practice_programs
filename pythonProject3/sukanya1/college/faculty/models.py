from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=15)
    address=models.TextField(max_length=15)
    contact=models.IntegerField(max_length=10)



