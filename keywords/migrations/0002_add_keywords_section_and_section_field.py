# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'KeywordSection'
        db.create_table('keywords_keywordsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('keywords', ['KeywordSection'])

        # Adding field 'Keyword.section'
        db.add_column('keywords_keyword', 'section', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='keywords', null=True, to=orm['keywords.KeywordSection']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'KeywordSection'
        db.delete_table('keywords_keywordsection')

        # Deleting field 'Keyword.section'
        db.delete_column('keywords_keyword', 'section_id')


    models = {
        'keywords.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'keywords'", 'null': 'True', 'to': "orm['keywords.KeywordSection']"})
        },
        'keywords.keywordpost': {
            'Meta': {'object_name': 'KeywordPost'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keyword_posts'", 'to': "orm['keywords.Keyword']"})
        },
        'keywords.keywordsection': {
            'Meta': {'object_name': 'KeywordSection'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['keywords']
