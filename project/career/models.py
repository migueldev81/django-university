from django.db import models

# Create your models here.


class Career(models.Model):
    name = models.CharField(max_length=35)
    code = models.CharField(max_length=35, primary_key=True)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)
