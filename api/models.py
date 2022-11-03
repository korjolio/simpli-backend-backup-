from django.db import models

# Create your models here.

class Company(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)