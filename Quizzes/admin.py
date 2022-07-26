from django.contrib import admin
from .models import QuestionBank, Quizattempts

class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ('course','assessment','weightage','question','marks','op1','op2','op3','op4','ans')


admin.site.register(QuestionBank,QuestionBankAdmin)


class QuizattemptsAdmin(admin.ModelAdmin):
    list_display = ('course','assessment','student','attempted')


admin.site.register(Quizattempts, QuizattemptsAdmin)
