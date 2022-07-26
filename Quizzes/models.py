from django.db import models

import sys
sys.path.append('../')

from Users.models import Courses, Students


class QuestionBank(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=10)
    weightage = models.FloatField("Weightage of assessment")
    question = models.CharField(max_length=5000)
    marks = models.IntegerField("Maximum marks for question")
    op1 = models.CharField("Option 1", max_length=500)
    op2 = models.CharField("Option 2", max_length=500)
    op3 = models.CharField("Option 3", max_length=500, null=True, blank=True)
    op4 = models.CharField("Option 4", max_length=500, null=True, blank=True)
    ans = models.CharField("Answer", max_length=500)


class Quizattempts(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=10)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    attempted = models.BooleanField(default=False)
