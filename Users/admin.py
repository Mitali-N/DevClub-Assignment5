from django.contrib import admin
from .models import Courses, Instructors, Students, Student_RegistrationTable, Instructor_RegistrationTable


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course','course_desc','credit')


admin.site.register(Courses, CoursesAdmin)


class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('instructor_id','name')


admin.site.register(Instructors, InstructorsAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('student_id','name')


admin.site.register(Students, StudentsAdmin)


class Instructor_RegistrationTableAdmin(admin.ModelAdmin):
    list_display = ('instructor_id','course_id')


admin.site.register(Instructor_RegistrationTable, Instructor_RegistrationTableAdmin)


class Student_RegistrationTableAdmin(admin.ModelAdmin):
    list_display = ('student_id','course_id')


admin.site.register(Student_RegistrationTable, Student_RegistrationTableAdmin)
