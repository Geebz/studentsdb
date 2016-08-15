# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Student, Group, Exam
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
from functools import partial
from django.forms.models import modelformset_factory


class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        group = Group.objects.filter(leader=self.instance)
        if len(group) > 0 and self.cleaned_data['student_group'] != group[0]:
            raise ValidationError(u'Студент є старостою іншою групою', code='invalid')
        return self.cleaned_data['student_group']


class GroupFormAdmin(ModelForm):

    def clean_leader(self):
        try:
            group = self.cleaned_data['leader'].student_group
            if group and group != self.instance:
                raise ValidationError(u'Студент навчається в іншій групі', code='invalid')
            return self.cleaned_data['leader']
        except AttributeError:
            return self.cleaned_data['leader']


class StudentModel(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    actions = ['object_copy']

    form = StudentFormAdmin

    def get_changelist_formset(self, request, **kwargs):
        defaults = {
            "formfield_callback": partial(super(StudentModel, self).formfield_for_dbfield, request=request),
            "form": StudentFormAdmin,
        }
        defaults.update(kwargs)
        return modelformset_factory(Student,
                                    extra=0,
                                    fields=self.list_editable, **defaults)

    def object_copy(self, request, queryset):
        for q in queryset:
            q.id = None
            q.save()
    object_copy.short_description = u'Копіювання студента'

    def get_view_on_site_url(self, obj=None):
        return reverse('students_edit', kwargs={'pk': obj.id})


class GroupModel(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title', 'leader', 'notes']

    form = GroupFormAdmin

    def get_changelist_formset(self, request, **kwargs):
        defaults = {
            "formfield_callback": partial(super(GroupModel, self).formfield_for_dbfield, request=request),
            "form": GroupFormAdmin,
        }
        defaults.update(kwargs)
        return modelformset_factory(Group,
                                    extra=0,
                                    fields=self.list_editable, **defaults)

    def get_view_on_site_url(self, obj=None):
        return reverse('groups_edit', kwargs={'pk': obj.id})

# Register your models here.
admin.site.register(Student, StudentModel)
admin.site.register(Group, GroupModel)
admin.site.register(Exam)

