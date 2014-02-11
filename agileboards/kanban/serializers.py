"""
agileboards.kanban.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from rest_framework import serializers

from . import models


class Ticket(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ('id', 'name', 'progress')


class Column(serializers.ModelSerializer):
    tickets = Ticket(many=True, allow_add_remove=True)

    class Meta:
        model = models.Column
        fields = ('id', 'name', 'tickets')


class Project(serializers.ModelSerializer):
	columns = Column(many=True, allow_add_remove=True)

	class Meta:
		model = models.Project
		fields = ('id', 'name', 'columns')

