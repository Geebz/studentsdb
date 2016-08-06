# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Group
from Classes.PaginatorCustom import PaginatorCustom,PageNotInteger,EmptyPage
# Views for groups

def groups_list(request):
    groups = Group.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader', 'id'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    else:
        groups = groups.order_by('title')
    paginator = PaginatorCustom(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    return render(request, 'students/groups.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Groups Edit %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Groups Delete %s</h1>' % gid)