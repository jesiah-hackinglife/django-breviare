# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table('breviare_urls_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('link_short', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('breviare_urls', ['Link'])

        # Adding model 'Click'
        db.create_table('breviare_urls_click', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['breviare_urls.Link'])),
            ('clicked_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('clicked_by', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('refer', self.gf('django.db.models.fields.URLField')(default='Direct', max_length=500)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('breviare_urls', ['Click'])

    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table('breviare_urls_link')

        # Deleting model 'Click'
        db.delete_table('breviare_urls_click')

    models = {
        'breviare_urls.click': {
            'Meta': {'object_name': 'Click'},
            'clicked_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'clicked_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['breviare_urls.Link']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'refer': ('django.db.models.fields.URLField', [], {'default': "'Direct'", 'max_length': '500'})
        },
        'breviare_urls.link': {
            'Meta': {'object_name': 'Link'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'link_short': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['breviare_urls']