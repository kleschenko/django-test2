# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActionsEntry'
        db.create_table('contacts_actionsentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('model_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('contacts', ['ActionsEntry'])


    def backwards(self, orm):
        # Deleting model 'ActionsEntry'
        db.delete_table('contacts_actionsentry')


    models = {
        'contacts.actionsentry': {
            'Meta': {'object_name': 'ActionsEntry'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['contacts']