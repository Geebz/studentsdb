# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Exam
# from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from Classes.PaginatorCustom import PaginatorCustom, EmptyPage, PageNotInteger

# Views for exams


def exams_list(request):
    exams = Exam.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'name', 'teacher'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
    else:
        exams = exams.order_by('name')
    return render(request, 'students/exams.html', {'exams': exams})
