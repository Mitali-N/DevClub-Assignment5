from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    course = models.CharField(max_length=6,primary_key=True)
    course_desc = models.CharField(max_length=55)
    credit = models.FloatField("credits",blank=True,default=0.0)


class Instructors(models.Model):
    instructor_id = models.CharField(max_length=6,primary_key=True, help_text="same as username")
    username = models.ForeignKey(User, on_delete=models.CASCADE, help_text="same as instructor id")                    
    name = models.CharField(max_length=55)


class Students(models.Model):
    student_id = models.CharField(max_length=6,primary_key=True, help_text="same as username")                 
    username = models.ForeignKey(User, on_delete=models.CASCADE, help_text="same as student id")                    
    name = models.CharField(max_length=55)

class Student_RegistrationTable(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    

class Instructor_RegistrationTable(models.Model):
    instructor_id = models.ForeignKey(Instructors, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)