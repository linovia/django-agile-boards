
from django.views import generic
from rest_framework import viewsets

from . import models, serializers


#
# REST API VIEWS
#

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    queryset = models.Project.objects.all()
    serializer_class = serializers.Project
    paginate_by = None

    def pre_save(self, project):
        for i, column in enumerate(project._related_data['columns']):
            column.order = i
            for j, ticket in enumerate(column._related_data['tickets']):
                ticket.order = j


#
# REGULAR VIEWS
#

class Project(generic.DetailView):
    model = models.Project
    template_name = "board.html"
    pk_url_kwarg = 'project_id'

    def get_context_data(self, **kwargs):
        context = super(Project, self).get_context_data(**kwargs)
        context['columns'] = models.Column.objects.filter(project=self.object)
        return context


class ColumnCreation(generic.CreateView):
    model = models.Column
    template_name = "column/edit.html"
