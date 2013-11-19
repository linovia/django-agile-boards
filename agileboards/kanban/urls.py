"""
agileboards.kanban.urls
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.conf.urls import patterns, url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

urlpatterns = patterns('',

    url(r'^(?P<project_id>\d+)/$',
        views.Project.as_view(),
        name="homepage"),

    url(r'^(?P<project_id>\d+)/columns/new/$',
        views.ColumnCreation.as_view(),
        name="new-column"),

    url(r'^',
        include(router.urls)),

    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
)
