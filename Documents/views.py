from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Document

import sys
sys.path.append('../')

from Users.models import Courses

def docs(request):
    coursedocs = Document.objects.filter(course=request.session['course'])
    if request.method=="POST":
        return redirect('upload')
    return render(request,'documents/showdocs.html',{'coursedocs':coursedocs})



def upload(request):
    if request.method=="POST":
        if request.POST['docname'] and request.FILES['document']:
            doctable = Document()
            doctable.docname = request.POST['docname']
            doctable.document = request.FILES['document']
            doctable.course = Courses.objects.get(course= request.session['course'])
            doctable.save()
            messages.success(request,("File uploaded successfully!"))
            return redirect('docs')
    return render(request,'documents/uploaddocs.html',{})