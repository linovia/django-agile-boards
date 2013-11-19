"""
agileboards.kanban.admin
~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.contrib import admin

from .models import Ticket, Column, Project


class TicketAdmin(admin.ModelAdmin):
    pass


class ColumnAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Project, ProjectAdmin)
