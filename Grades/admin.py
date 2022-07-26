from django.contrib import admin
from .models import Marks, Grades


class MarksAdmin(admin.ModelAdmin):
    list_display = ('studentID','courseID','assessment','weightage','total_marks','marks')

admin.site.register(Marks, MarksAdmin)


class GradesAdmin(admin.ModelAdmin):
    list_display = ('studentID','courseID','grade')


admin.site.register(Grades, GradesAdmin)
