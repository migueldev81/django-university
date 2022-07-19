from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=35)
    code = models.CharField(max_length=35, primary_key=True)
    credits = models.PositiveSmallIntegerField(default=5)
    teacher = models.CharField(max_length=35)
    def __str__(self):
      txt = "{0}"
      return txt.format(self.name)