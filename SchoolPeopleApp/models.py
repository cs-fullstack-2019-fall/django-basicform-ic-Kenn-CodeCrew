from django.db import models
from django.utils import timezone


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200, default="")
    county = models.CharField(max_length=200, default="")
    students = models.IntegerField(default=0)
    dateOpened = models.DateField(default="")
    def __str__(self):
        return f"{self.name} is in {self.county} with {self.students} students and opened on {self.dateOpened}"

class People(models.Model):
    name = models.CharField(max_length=200, default="")
    age = models.DecimalField(decimal_places=3, max_digits=7)
    dob = models.DateTimeField(default=timezone.now())