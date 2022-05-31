from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    address = models.TextField()
    contact = models.IntegerField()

# Create your models here.
