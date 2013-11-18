
from django.views.generic import DetailView
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


#
# REGULAR VIEWS
#

class ProjectView(DetailView):
    model = models.Project
    template_name = "board.html"
    pk_url_kwarg = 'project_id'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['columns'] = models.Column.objects.filter(project=self.object)
        return context
