
from itertools import groupby

from django.views.generic import DetailView

from rest_framework import viewsets

from .serializers import TicketSerializer
from .models import Ticket, Column, Project


#
# REST API VIEWS
#

class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    paginate_by = None


#
# REGULAR VIEWS
#

class ProjectView(DetailView):
    model = Project
    template_name = "board.html"
    pk_url_kwarg = 'project_id'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['columns'] = Column.objects.filter(project=self.object)
        return context
