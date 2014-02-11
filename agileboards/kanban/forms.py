"""
agileboards.kanban.forms
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models


class Column(forms.ModelForm):

    def __init__(self, project_id=None, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self._project_id = project_id
        return super(Column, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.project_id = self._project_id
        return super(Column, self).save(*args, **kwargs)

    class Meta:
        model = models.Column
        fields = ('name', 'order')
