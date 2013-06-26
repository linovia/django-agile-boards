from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField(max_length=64)
    order = models.IntegerField()

    class Meta:
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')
        ordering = ('order')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Ticket(models.Model):
    name = models.CharField(max_length=32)
    progress = models.IntegerField()
    status = models.ForeignKey(Column)
    order = models.IntegerField()

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ('status', 'order')

    def __str__(self):
        return self.name
