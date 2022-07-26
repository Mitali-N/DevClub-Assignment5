from django.shortcuts import render, redirect
from .models import Announcements, Message
from django.contrib import messages
from django.db.models import Q

import sys
sys.path.append('../')

from Users.models import Instructors,Courses, Students

def announce(request):
    all_announce = Announcements.objects.filter(course=request.session['course'])
        
    inst_ids=[]
    for item in all_announce:
        a = str(item.instructor).strip("Instructor Object ")
        b = a.strip("(")
        inst_ids.append(b.strip(")"))

    d=[]
    for instid in inst_ids:
        instrname = Instructors.objects.get(instructor_id=instid)
        d.append(instrname)

    if request.method=="POST":
        return redirect('makeannounce')
        
    return render(request,'communications/announce.html',{'query':all_announce,'instnames':d,'instids':inst_ids})
    
def makeannounce(request):
    if request.method=="POST":
        if request.POST['announce']:
            add = Announcements()
            add.announcement = request.POST['announce']
            add.instructor = Instructors.objects.get(instructor_id=request.user.username)
            add.course = Courses.objects.get(course=request.session['course'])
            add.save()
            messages.success(request,(f"Announcement made successfully: \n {request.POST['announce']} "))
            return redirect('announcements')
    return render(request, 'communications/makeannounce.html',{})

def messenger(request):
    if request.method == "POST":
        if request.POST['text']=="+ New Message":
            return redirect('newmessage')
        else:
            request.session['textee'] = request.POST['recipient']
            table = Message()
            table.message = request.POST['text']
            table.to = request.POST['recipient']
            table.sender = request.user.username
            table.save()
            return redirect('messages')
    messagers = []
    messages_ = Message.objects.filter(Q(sender=request.user.username) | Q(to=request.user.username))
    for message in messages_:
        if str(message.to)!=request.user.username and str(message.to) not in messagers:
            messagers.append(str(message.to))
        elif str(message.sender)!=request.user.username and str(message.sender) not in messagers:
            messagers.append(str(message.sender))

    return render(request,'communications/messenger.html',{'messagers':messagers,'messages_':messages_})

def newmessage(request):
    students = Students.objects.all()
    instr = Instructors.objects.all()
    s=[]
    i=[]
    for student in students:
        s.append(student.student_id)
    for inst in instr:
        i.append(inst.instructor_id)

    if request.method=="POST":
        if request.POST['recipient']:
            if (request.POST['recipient'] in i) or (request.POST['recipient'] in s):
                request.session['textee'] = request.POST['recipient']
                table = Message()
                table.message = request.POST['new']
                table.to = request.POST['recipient']
                table.sender = request.user.username
                table.save()
                messages.success(request, ("Message sent!"))
                return redirect('messages')
            else:
                messages.success(request, ("Invalid recipient ID!"))
                return redirect('newmessage')
    return render(request,'communications/newmessage.html',{})

'''
<div class="accordion" id="accordionExample">
    {% for messager in messagers %}
    <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne_{{ messager }}">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne_{{ messager }}" aria-expanded="true" aria-controls="collapseOne_{{ messager }}">
                {{ messager }}
            </button>
        </h2>
        <div id="collapseOne_{{ messager }}" class="accordion-collapse collapse show" aria-labelledby="headingOne_{{ messager }}" data-bs-parent="#accordionExample">
            <div class="accordion-body">
            <div data-bs-spy="scroll" data-bs-target="#headingOne_{{ messager }}" data-bs-offset="0" data-bs-smooth-scroll="true" class="scrollspy-example" tabindex="0">
                {% for message in messages %}
                    {% if message.sender==messager and message.to==request.user.username %}
                        <div class="alert alert-light" role="alert">
                            {{ message.date }} {{ message.message }} {{ message.time }}
                        </div>  
                    {% endif %}
                    {% if message.sender==request.user.username and message.to==messager %}
                        <div class="alert alert-info" role="alert">
                            {{ message.date }} {{ message.message }} {{ message.time }}
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        </div>
    </div>
    {% endfor %}
</div>
'''