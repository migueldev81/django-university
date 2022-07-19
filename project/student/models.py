from statistics import mode
from django.db import models
from career.models import Career

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=35)
    ci = models.CharField(max_length=8, primary_key=True)
    date = models.DateField()
    sexs = [('F', 'Female'), ('M', 'Male')]
    sex = models.CharField(max_length=10, choices=sexs, default='F')
    career = models.ForeignKey(Career,
                               null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    validiy = models.BooleanField(default=True)
    def __str__(self):
      txt = "{0}"
      return txt.format(self.name)