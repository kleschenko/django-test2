# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.priority'
        db.add_column('logs_entry', 'priority',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.priority'
        db.delete_column('logs_entry', 'priority')


    models = {
        'logs.entry': {
            'Meta': {'object_name': 'Entry'},
            'dtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['logs']