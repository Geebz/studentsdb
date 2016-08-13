# -*- coding: utf-8 -*-
from __future__ import division
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from ..models import Student, Group
from django.core.urlresolvers import reverse
# from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from Classes.PaginatorCustom import PaginatorCustom, EmptyPage, PageNotInteger
from datetime import datetime
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, DeleteView
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions
# Views for student


def students_list(request):
    students = Student.objects.all()
    # order student list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    else:
        students = students.order_by('last_name')

    # paginator = Paginator(students, 3)
    # page = request.GET.get('page')
    # try:
    #     students = paginator.page(page)
    # except PageNotAnInteger:
    #     students = paginator.page(1)
    # except EmptyPage:
    #     students = paginator.page(paginator.num_pages)

    paginator = PaginatorCustom(students, 4)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.attrs = {'novalidate': ''}

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )


class StudentUpdateForm(StudentForm):
    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})


class StudentAddForm(StudentForm):
    def __init__(self, *args, **kwargs):
        super(StudentAddForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('students_add')


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentAddForm

    def get_success_url(self):
        messages.success(self.request, u'Студента успішно додано!')
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Додавання студента'
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Додавання студента відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentCreateView, self).post(request, *args, **kwargs)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        messages.success(self.request, u'Студента успішно відредаговано :)')
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u'Редагування студента'
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Редагування студента відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, u'Видалення студента пройшло успішно')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, u'Видалення студента відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentDeleteView, self).post(request, *args, **kwargs)

