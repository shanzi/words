# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Keyword'
        db.create_table('keywords_keyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('keywords', ['Keyword'])

        # Adding model 'KeywordPost'
        db.create_table('keywords_keywordpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.related.ForeignKey')(related_name='keyword_posts', to=orm['keywords.Keyword'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('keywords', ['KeywordPost'])


    def backwards(self, orm):
        
        # Deleting model 'Keyword'
        db.delete_table('keywords_keyword')

        # Deleting model 'KeywordPost'
        db.delete_table('keywords_keywordpost')


    models = {
        'keywords.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'})
        },
        'keywords.keywordpost': {
            'Meta': {'object_name': 'KeywordPost'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keyword_posts'", 'to': "orm['keywords.Keyword']"})
        }
    }

    complete_apps = ['keywords']
