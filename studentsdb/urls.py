from django.conf.urls import include, url, patterns
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView, StudentCreateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', StudentCreateView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name='groups_delete'),
    url(r'^journal/$', 'students.views.journal.journal_list', name='journal'),
    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
    url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': MEDIA_ROOT}))

