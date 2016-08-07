# -*- coding: utf-8 -*-

from django.db import models


class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name = u'Екзамен'
        verbose_name_plural = u'Екзамени'

    name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u'Дисципліна'
        )

    date = models.DateField(
        blank=False,
        verbose_name=u'Дата проведення',
        null=True
    )

    teacher = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u'Викладач'
    )

    groups = models.ManyToManyField(
        'Group',
        verbose_name=u'Групи',
        blank=False,
    )

    def __unicode__(self):
        return '%s' % self.name
