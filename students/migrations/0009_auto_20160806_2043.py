# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20160727_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0456\u043d\u0430')),
                ('date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('teacher', models.CharField(max_length=255, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
            ],
            options={
                'verbose_name': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='exam_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0415\u043a\u0437\u0430\u043c\u0435\u043d', to='students.Exam', null=True),
        ),
    ]
