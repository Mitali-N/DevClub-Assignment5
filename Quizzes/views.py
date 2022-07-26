from django.shortcuts import render, redirect
from django.contrib import messages
from .models import QuestionBank, Quizattempts

import sys
sys.path.append('../')

from Grades.models import Marks
from Users.models import Students, Courses, Student_RegistrationTable

def quiz(request):
    questions = QuestionBank.objects.filter(course=request.session['course'],assessment=request.session['assessment'])

    total_marks=0
    for q in questions:
        weight = q.weightage
        total_marks+=int(q.marks)
    
    data = Quizattempts.objects.get(course=request.session['course'],student=request.user.username,assessment=request.session['assessment'])
    if data.attempted == True:
        return render(request, 'quiz/alreadyattempted.html')

    if request.method=="POST":
        score=0
        wrong=0
        correct=0
        total_marks=0
        for q in questions:
            weight = q.weightage
            total_marks+=int(q.marks)
            if q.ans == request.POST.get(q.question):
                score+=int(q.marks)
                correct+=1
            else:
                wrong+=1
        
        table = Marks()
        table.studentID = Students.objects.get(student_id=request.user.username)
        table.courseID = Courses.objects.get(course= request.session['course'])
        table.assessment = request.session['assessment']
        table.weightage = weight
        table.total_marks = total_marks
        table.marks = score
        table.save()

        update = Quizattempts.objects.get(course= request.session['course'],student=request.user.username,assessment=request.session['assessment'])
        update.attempted = True
        update.save()
        
        context={
            'score' : score,
            'correct' : correct,
            'wrong' : wrong,
            'max_marks' : total_marks,
            'weightage' : weight
        }

        request.session['scoredict']=context
        return redirect('results')

    return render(request, 'quiz/test.html',{'questions':questions,'max':total_marks,'weightage':weight})

def quizlist(request):
    if request.method=="POST":
        request.session['assessment'] = request.POST['assessment']
        return redirect('test')
    record = QuestionBank.objects.filter(course=request.session['course'])
    l=[]
    for rec in record:
        if str(rec.assessment) not in l:
            l.append(str(rec.assessment))
    return render(request,'quiz/choosequiz.html',{'assessmentlist':l})

def result(request):
    context= request.session['scoredict']
    return render(request,'quiz/result.html',context)

def makequiz(request):
    if request.method=="POST":
        students = Student_RegistrationTable.objects.filter(course_id=request.session['course'])
        for student in students:
            a=str(student.student_id).strip("Students object ")
            b=a.strip("(")
            c=b.strip(")")
            table = Quizattempts()
            table.student = Students.objects.get(student_id=c)
            table.course = Courses.objects.get(course=request.session['course'])
            table.assessment = request.POST['assessment']
            table.save()

        request.session['assessment'] = request.POST['assessment']
        request.session['weightage'] = request.POST['weightage']
        return redirect('addques')
    return render(request, 'quiz/createquiz.html')

def addques(request):
    if request.method=="POST":
        quiz = QuestionBank()
        quiz.course = Courses.objects.get(course=request.session['course'])
        quiz.assessment = request.session['assessment']
        quiz.weightage = request.session['weightage']
        quiz.question = request.POST['question']
        quiz.marks = request.POST['marks']
        quiz.op1 = request.POST['op1']
        quiz.op2 = request.POST['op2']
        quiz.op3 = request.POST['op3']
        quiz.op4 = request.POST['op4']
        quiz.ans = request.POST['ans']
        quiz.save()
        messages.success(request,("Question added."))
        return redirect('addques')
    return render(request,'quiz/addques.html')

def quizcreated(request):
    return render(request,'quiz/created.html')
