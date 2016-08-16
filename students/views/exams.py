# -*- coding: utf-8 -*-

from ..models import Exam
from django.shortcuts import render
from django.http import HttpResponse
from Classes.CustomForm import CustomForm
from django.http.response import HttpResponseRedirect
from django.views.generic import DeleteView, CreateView, UpdateView
from django.contrib import messages
from django.core.urlresolvers import reverse

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


class ExamCreateForm(CustomForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExamCreateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('exams_add')

class ExamUpdateForm(CustomForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExamUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('exams_edit', kwargs={'pk':kwargs['instance'].id})


class ExamCreateView(CreateView):
    model = Exam
    template_name = 'template_add_edit.html'
    form_class = ExamCreateForm

    def get_context_data(self, **kwargs):
        context = super(ExamCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Додавання іспиту'
        return context

    def get_success_url(self):
        messages.success(self.request, u'Іспит успішно додано!')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Додавання іспита відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(ExamCreateView, self).post(request, *args, **kwargs)


class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'template_add_edit.html'
    form_class = ExamUpdateForm

    def get_context_data(self, **kwargs):
        context = super(ExamUpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Редагування іспиту'
        return context

    def get_success_url(self):
        messages.success(self.request, u'Іспит успішно Відредаговано!')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Редагування іспита відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'template_delete_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ExamDeleteView, self).get_context_data(**kwargs)
        context['title'] = u'Видалення іспиту'
        context['name'] = u'іспит'
        context['url'] = reverse('exams_delete', kwargs={'pk': kwargs['object'].id})
        return context

    def get_success_url(self):
        messages.success(self.request, u'Іспит успішно Видалено!')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Видалення іспита відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(ExamDeleteView, self).post(request, *args, **kwargs)
