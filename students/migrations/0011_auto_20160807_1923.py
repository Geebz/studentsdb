# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20160807_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='groups',
            field=models.ManyToManyField(to='students.Group', verbose_name='\u0415\u043a\u0437\u0430\u043c\u0435\u043d'),
        ),
    ]
