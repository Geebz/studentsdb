# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Views for student

def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Андрій',
         'last_name': u'Ковтун',
         'ticket': 235,
         'image': 'img/bin.png'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/pivo.png'},
        {'id': 3,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/oxx.png'},
    )
    return render(request,'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Students Delete %s</h1>' % sid)