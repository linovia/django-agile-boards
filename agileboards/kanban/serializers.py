
from rest_framework import serializers

from . import models


class Ticket(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ('id', 'name', 'progress', 'order', 'status')


class Column(serializers.ModelSerializer):
    tickets = Ticket(many=True, allow_add_remove=True)

    class Meta:
        model = models.Column
        fields = ('id', 'name', 'order', 'tickets')


class Project(serializers.ModelSerializer):
	columns = Column(many=True, allow_add_remove=True)

	class Meta:
		model = models.Project
		fields = ('id', 'name', 'columns')

