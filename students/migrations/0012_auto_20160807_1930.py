# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20160807_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='groups',
            field=models.ManyToManyField(to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0438'),
        ),
    ]
