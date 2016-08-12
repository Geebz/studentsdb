# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from studentsdb.mail_settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib import messages
from django.views.generic.edit import FormView



class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):

        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))

    from_email = forms.EmailField(
        label=u'Ваша електронна адресса'
    )

    subject = forms.CharField(
        label=u'Заголовок',
        max_length=128
    )

    message = forms.CharField(
        label=u'Повідомлення',
        max_length=2560,
        widget=forms.Textarea
    )


# def contact_admin(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_mail = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']+'\nmail: '+from_mail
#             try:
#                 send_mail(subject, message, from_mail, [ADMIN_EMAIL])
#             except Exception:
#                 messages.warning(request, u'Під час відправки листа відбулась неочікувана помилка.'
#                                           u' Будь-ласка спробуйте пізніше')
#             else:
#                 messages.success(request, u'Листа успішно відправлено!')
#             return HttpResponseRedirect(reverse('contact_admin'))
#     else:
#         form = ContactForm
#     return render(request, 'contact_admin/form.html', {'form': form})

class ContactView(FormView):
    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_admin')

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        from_mail = form.cleaned_data['from_email']
        message = form.cleaned_data['message'] + '\nmail: ' + from_mail
        try:
            send_mail(subject, message, from_mail, [ADMIN_EMAIL])
        except Exception:
            messages.warning(self.request, u'Під час відправки листа відбулась неочікувана помилка.'
                                           u'Будь-ласка спробуйте пізніше')
        else:
            messages.success(self.request, u'Листа успішно відправлено!')

        return super(ContactView, self).form_valid(form)
