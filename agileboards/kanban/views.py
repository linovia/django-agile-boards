
from rest_framework import viewsets
from .serializers import TicketSerializer
from .models import Ticket


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    paginate_by = None
