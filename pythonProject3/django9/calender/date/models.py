from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    address=models.TextField(max_length=20)


# Create your models here.
