# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NicEditImage'
        db.create_table(u'nicedit_niceditimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'nicedit', ['NicEditImage'])


    def backwards(self, orm):
        # Deleting model 'NicEditImage'
        db.delete_table(u'nicedit_niceditimage')


    models = {
        u'nicedit.niceditimage': {
            'Meta': {'object_name': 'NicEditImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['nicedit']