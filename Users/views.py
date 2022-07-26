from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Students, Student_RegistrationTable, Instructors, Instructor_RegistrationTable, Courses

import sys
sys.path.append('../')

from Grades.models import Marks, Grades

def usertype(request,id):
    for obj in Instructors.objects.all():
        if obj.instructor_id==id:
            request.session['usertype'] = 'instructor'
    for obj in Students.objects.all():
        if obj.student_id==id:
            request.session['usertype'] = 'student'


def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            usertype(request,username)
            if request.user.username=="admin":
                return redirect('/admin/')
            else:
                return redirect('home')
        else:
            messages.success(request,("Incorrect username or password. Please try again"))
            return redirect('login')
    else:
        return render(request,'registration/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("Logged out successfully."))
    return redirect('login')



def home(request):
    #usertype(request.user.username)
    request.session['textee']=""
    if request.session['usertype']=='student':
        studentid = request.user.username
        studentinfo= Students.objects.get(student_id=studentid)
        studentcourses = Student_RegistrationTable.objects.filter(student_id=studentid)
        
        if request.method=="POST":
            request.session['course'] = request.POST['course']
            return redirect('coursepage')

        l1=[]
        for element in studentcourses:
            a = str(element.course_id).strip("Courses Object ")
            b = a.strip("(")
            l1.append(b.strip(")"))

        d={}
        for c in l1:
            courserec = Courses.objects.get(course=c)
            desc = str(courserec.course_desc)
            d[c]=desc
        return render(request, 'registration/home.html',{'info':studentinfo,'courses':d})
    
    elif request.session['usertype']=='instructor':
        inst_id = request.user.username
        inst_info= Instructors.objects.get(instructor_id=inst_id)
        instcourses = Instructor_RegistrationTable.objects.filter(instructor_id=inst_id)
        inst_courses=[]
        for ic in instcourses:
            a=str(ic.course_id).strip("Courses Object ")
            b = a.strip("(")
            inst_courses.append(b.strip(")"))
        
        if request.method=="POST":
            request.session['course'] = request.POST['course']
            return redirect('coursepage')
        return render(request, 'registration/home.html',{'info':inst_info,'courses':inst_courses})


def course_page(request):
    courseinfo = Courses.objects.get(course=request.session['course'])
    return render(request, 'registration/coursepage.html',{'courseinfo':courseinfo})

def gradesheet(request):
    studentid = request.user.username
    studentGrades = Grades.objects.filter(studentID=studentid)
    l=[]
    for rec in studentGrades:
        a = (str(rec.courseID)).strip("Course object ")
        b = a.strip("(")
        l.append(b.strip(")"))

    studentinfo = Students.objects.get(student_id= studentid)

    credits = []
    d = {}
    for c in l:
        cours = Courses.objects.get(course=c)
        credits.append(cours.credit)
        d[c] = cours.credit
    
    totalgrades = 0
    totalcreds = 0
    for key in d:
        for grades in studentGrades:
            if str(grades.courseID) == ("Courses object ("+key+")"):
                totalgrades += float(grades.grade)*float(d[key])
                totalcreds += float(d[key])
    
    if totalcreds!=0:
        cg = totalgrades/totalcreds
    else:
        cg = 0

    return render(request, 'registration/grades.html',{'studentGrades':studentGrades,'courses':l,'studentinfo':studentinfo,'credits':credits,'cg':cg})

def marks(request):
    if request.session['usertype']=='student':
        studentid = request.user.username
        courseid = request.session['course']
        studentMarks = Marks.objects.filter(studentID=studentid).filter(courseID=courseid)
        studentinfo = Students.objects.get(student_id=studentid)
        return render(request, 'registration/marks.html',{'table':studentMarks,'info':studentinfo,'studentid':studentid})
    
    elif request.session['usertype']=='instructor':
        if request.method=="POST":
            if request.POST['marks']=="Upload marks for assessment":
                return redirect('uploadmarks')
            elif request.POST['marks']=="Upload Final Grades":
                return redirect('uploadfinal')
        return render(request,'registration/uploadgrades.html',{})

def uploadmarks(request):
    if request.method=="POST":
        if request.POST['studentID'] and  request.POST['assessment'] and  request.POST['weightage'] and  request.POST['total_marks'] and  request.POST['marks']:
            table = Marks()
            table.studentID = Students.objects.get(student_id=request.POST['studentID'])
            table.courseID = Courses.objects.get(course= request.session['course'])
            table.assessment = request.POST['assessment']
            table.weightage = request.POST['weightage']
            table.total_marks = request.POST['total_marks']
            table.marks = request.POST['marks']
            table.save()
            messages.success(request,("Data entered"))
            return redirect('uploadmarks')
    return render(request, 'registration/uploadmarks.html',{})

def uploadfinal(request):
    if request.method=="POST":
        if request.POST['studentID'] and  request.POST['grade']:
            table = Grades()
            table.studentID = Students.objects.get(student_id=request.POST['studentID'])
            table.courseID = Courses.objects.get(course= request.session['course'])
            table.grade = int(request.POST['grade'])
            table.save()
            messages.success(request,("Data entered"))
            return redirect('uploadfinal')
    return render(request,'registration/uploadfinal.html',{})