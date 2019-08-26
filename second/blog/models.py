from django.db import models
from django.conf import settings
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

