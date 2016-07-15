# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def journal_list(request):
    journals = (
        {
            'id':1,
            'name':u'Артюх Євген',
            'checked':{1,10,15}
        },
        {
            'id': 2,
            'name': u'Андрій Ковтун',
            'checked': {3, 4, 17,23}
        },
        {
            'id': 3,
            'name': u'Артюх Євген',
            'checked': {1, 11, 13,19}
        }
    )
    return render(request, 'students/journal.html',{'journals':journals})