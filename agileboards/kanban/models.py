from django.utils.translation import ugettext_lazy as _
from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
