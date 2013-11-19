# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'kanban_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'kanban', ['Project'])

        # Adding model 'Column'
        db.create_table(u'kanban_column', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'columns', to=orm['kanban.Project'])),
        ))
        db.send_create_signal(u'kanban', ['Column'])

        # Adding model 'Ticket'
        db.create_table(u'kanban_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('progress', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'tickets', to=orm['kanban.Column'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'kanban', ['Ticket'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'kanban_project')

        # Deleting model 'Column'
        db.delete_table(u'kanban_column')

        # Deleting model 'Ticket'
        db.delete_table(u'kanban_ticket')


    models = {
        u'kanban.column': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'Column'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'columns'", 'to': u"orm['kanban.Project']"})
        },
        u'kanban.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'kanban.ticket': {
            'Meta': {'ordering': "(u'status', u'order')", 'object_name': 'Ticket'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'progress': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tickets'", 'to': u"orm['kanban.Column']"})
        }
    }

    complete_apps = ['kanban']