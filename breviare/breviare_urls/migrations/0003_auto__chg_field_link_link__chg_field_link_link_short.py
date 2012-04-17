# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Link.link'
        db.alter_column('breviare_urls_link', 'link', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Link.link_short'
        db.alter_column('breviare_urls_link', 'link_short', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))
    def backwards(self, orm):

        # Changing field 'Link.link'
        db.alter_column('breviare_urls_link', 'link', self.gf('django.db.models.fields.URLField')(max_length=500))

        # Changing field 'Link.link_short'
        db.alter_column('breviare_urls_link', 'link_short', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))
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
            'link': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'link_short': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['breviare_urls']