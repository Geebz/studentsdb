# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student

# Views for student
def students_list(request):
    students = Student.objects.all()
    return render(request,'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Students Delete %s</h1>' % sid)