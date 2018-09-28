from __future__ import unicode_literals  
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30,default=None)
    last_name = models.CharField(max_length=30,default=None)
    contact = models.IntegerField(default=None)
    email = models.EmailField(max_length=50,default=None)
    age = models.IntegerField(default=None)
    grade = models.IntegerField(default=None)

class Category(models.Model):
    name = models.CharField(max_length=255,default=None)

class book(models.Model):
    title = models.CharField(max_length=255,default=None)
    publish_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Employee (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    class Meta:
        db_table = "employee"