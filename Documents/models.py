import sys
sys.path.append('../')

from django.db import models
from Users.models import Courses

class Document(models.Model):
    docname = models.CharField("Document name",max_length=55)
    document = models.FileField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)