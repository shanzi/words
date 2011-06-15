# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Picture'
        db.create_table('pictures_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medium', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('fullsize', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal('pictures', ['Picture'])

        # Adding model 'Comment'
        db.create_table('pictures_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['pictures.Picture'])),
        ))
        db.send_create_signal('pictures', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Picture'
        db.delete_table('pictures_picture')

        # Deleting model 'Comment'
        db.delete_table('pictures_comment')


    models = {
        'pictures.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['pictures.Picture']"})
        },
        'pictures.picture': {
            'Meta': {'object_name': 'Picture'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'fullsize': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['pictures']
