import sys
sys.path.append('../')


from django.db import models
from Users.models import Courses, Students


class Marks(models.Model):
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=25)
    weightage = models.FloatField(help_text="In percentage")
    total_marks = models.FloatField("maximum marks")
    marks = models.FloatField(null=True,blank=True)

class Grades(models.Model):
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True,blank=True)