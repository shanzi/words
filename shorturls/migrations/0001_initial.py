# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ShortUrl'
        db.create_table('shorturls_shorturl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('origin', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('shorturls', ['ShortUrl'])


    def backwards(self, orm):
        
        # Deleting model 'ShortUrl'
        db.delete_table('shorturls_shorturl')


    models = {
        'shorturls.shorturl': {
            'Meta': {'object_name': 'ShortUrl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['shorturls']
