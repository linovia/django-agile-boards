from django.conf.urls import patterns, include, url

from agileboards.kanban.views import ProjectView


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^(?P<project_id>\d+)/$', ProjectView.as_view(), name="homepage"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kanban/', include('agileboards.kanban.urls')),
)
