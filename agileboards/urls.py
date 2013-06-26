from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agileboards.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="board.html"), name="homepage"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^kanban/', include('agileboards.kanban.urls')),
)
