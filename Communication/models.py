from django.db import models

import sys
sys.path.append('../')

from Users.models import Instructors, Courses

class Announcements(models.Model):
    announcement = models.CharField(max_length=2000)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructors, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.CharField(max_length=6)
    to = models.CharField("Recipient",max_length=6)
    message = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    #is_read = models.BooleanField(default=False)