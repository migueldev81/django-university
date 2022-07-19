from django.db import models
from student.models import Student
from course.models import Course

# Create your models here.
class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    course = models.ForeignKey(Course,
                               null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
      txt = "{0} (Course: {1})"
      return txt.format(self.student, self.course)