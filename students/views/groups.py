# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
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