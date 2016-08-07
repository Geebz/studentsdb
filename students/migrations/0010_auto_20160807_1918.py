# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20160806_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='exam_group',
        ),
        migrations.AddField(
            model_name='exam',
            name='groups',
            field=models.ManyToManyField(to='students.Group', null=True, verbose_name='\u0415\u043a\u0437\u0430\u043c\u0435\u043d'),
        ),
    ]
