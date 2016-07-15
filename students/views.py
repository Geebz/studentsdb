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

# Views for groups

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'ФБ-32',
         'leader': {'id': 1, 'name': u'Олексій Санак'}},
        {'id': 2,
         'name': u'ФБ-31',
         'leader': {'id': 2, 'name': u'Євгеній Лупан'}},
        {'id': 3,
         'name': u'ФФ-32',
         'leader': {'id': 3, 'name': u'Оліфер Леонід'}},
    )
    return render(request,'students/groups.html', {'groups':groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, sid):
    return HttpResponse('<h1>Groups Edit %s</h1>' % sid)

def groups_delete(request, sid):
    return HttpResponse('<h1>Groups Delete %s</h1>' % sid)

def journal(request):
    return render(request, 'students/journal.html',{})