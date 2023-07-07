from django.db import models

# Create your models here.
class SignForm(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
