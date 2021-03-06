# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Group
from Classes.PaginatorCustom import PaginatorCustom, PageNotInteger, EmptyPage
from Classes.CustomForm import CustomForm
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
    return render(request, 'students/groups.html', {'groups': groups})


class GroupCreateForm(CustomForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupCreateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('groups_add')

    def clean_leader(self):
        if self.cleaned_data['leader']:
            raise ValidationError(u'Данна група тільки створюється. Додати старосту неможливо')
        # return self.cleaned_data['leader']


class GroupUpdateForm(CustomForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('groups_edit', kwargs={'pk': kwargs['instance'].id})

    def clean_leader(self):
        # print type(self.cleaned_data['title'])
        try:
            if self.cleaned_data['leader'].student_group != self.instance:
                raise ValidationError(u'Студент навчається в іншій групі')
            return self.cleaned_data['leader']
        except AttributeError:
            return self.cleaned_data['leader']


class GroupCreateView(CreateView):
    model = Group
    template_name = 'template_add_edit.html'
    form_class = GroupCreateForm

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Додавання групи'
        return context

    def get_success_url(self):
        messages.success(self.request, u'Групу успішно додано')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Додавання групи відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'template_add_edit.html'
    form_class = GroupUpdateForm

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Редагування групи'
        return context

    def get_success_url(self):
        messages.success(self.request, u'Групу успішно відредаговано')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Додавання групи відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'template_delete_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Видалення групи'
        context['name'] = u'групу'
        context['url'] = reverse('groups_delete', kwargs={'pk': kwargs['object'].id})
        return context

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