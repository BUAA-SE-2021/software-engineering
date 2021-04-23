from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
