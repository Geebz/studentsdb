# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20160724_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, blank=True, to='students.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='\u0406\u043c\u2019\u044f'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=255, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0441\u044c\u043a\u0438\u0439 \u043a\u0432\u0438\u0442\u043e\u043a'),
        ),
    ]
