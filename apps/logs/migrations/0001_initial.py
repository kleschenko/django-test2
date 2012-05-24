# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table('logs_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('meta', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('logs', ['Entry'])

    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table('logs_entry')

    models = {
        'logs.entry': {
            'Meta': {'object_name': 'Entry'},
            'dtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['logs']