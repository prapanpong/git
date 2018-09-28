from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Employee(models.Model):
    empID =models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contactName = models.CharField(max_length=20)

    class Meta:
        db_table = "employee"

