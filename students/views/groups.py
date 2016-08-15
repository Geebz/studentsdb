# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Group, Student
from Classes.PaginatorCustom import PaginatorCustom, PageNotInteger, EmptyPage
from django.http.response import HttpResponseRedirect
from django.views.generic import DeleteView, CreateView, UpdateView
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
    return render(request, 'group/groups.html', {'groups': groups})


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def clean_leader(self):
        if self.cleaned_data['leader']:
            raise ValidationError(u'В группі не має ні одного студента. Будь-ласка додайте хоча б одного')
        return self.cleaned_data['leader']


class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def clean_leader(self):
        # print type(self.cleaned_data['title'])
        if self.cleaned_data['leader'].student_group != self.instance:
            raise ValidationError(u'Студент навчається в іншій групі')
        else:
            return self.cleaned_data['leader']


class GroupCreateView(CreateView):
    model = Group
    template_name = 'group/groups_add_edit.html'
    form_class = GroupCreateForm

    def get_success_url(self):
        messages.success(self.request, u'Групу успішно додано')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Додавання групи відмінено')
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'group/groups_add_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        messages.success(self.request, u'Групу успішно відредаговано')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Додавання групи відмінено')
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'group/groups_confirm_delete.html'

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