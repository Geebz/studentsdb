# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Group
from Classes.PaginatorCustom import PaginatorCustom, PageNotInteger, EmptyPage
from django.http.response import HttpResponseRedirect
from django.views.generic import DeleteView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import ProtectedError
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

def groups_edit(request, pk):
    return HttpResponse('<h1>Groups Edit %s</h1>' % pk)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, u'Групу успішно видалено')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Видалення группи відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            try:
                return super(GroupDeleteView, self).post(request, *args, **kwargs)
            except ProtectedError:
                storage = messages.get_messages(request)
                for _ in storage:
                    pass
                messages.warning(self.request, u'Поки в группі є студенти видалення неможливе')
                return HttpResponseRedirect(reverse('groups_delete', kwargs={'pk': self.object.id}))
            except Exception:
                storage = messages.get_messages(request)
                for _ in storage:
                    pass
                messages.warning(self.request, u'Непередбачувана помилка. Будь-ласка спробуйте пізніше')
                return HttpResponseRedirect(reverse('home'))