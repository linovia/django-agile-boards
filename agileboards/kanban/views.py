
from django.views import generic
from django.http import HttpResponseRedirect
from rest_framework import viewsets

from . import models, serializers, forms


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
    pk_url_kwarg = "project_id"


class ColumnCreation(generic.CreateView):
    model = models.Column
    template_name = "columns/edit.html"
    form_class = forms.Column

    def form_valid(self, form):
        column = form.save(commit=False)
        column.project_id = self.kwargs['project_id']
        column.save()
        return HttpResponseRedirect(self.get_success_url())
