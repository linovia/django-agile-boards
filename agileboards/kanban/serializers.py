
from rest_framework import serializers

from .models import Ticket, Column


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'name', 'progress', 'order', 'status')


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'name', 'order')
