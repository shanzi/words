# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AuthMeta'
        db.create_table('socialauth_authmeta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('provider', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_email_filled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_profile_modified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('socialauth', ['AuthMeta'])

        # Adding model 'OpenidProfile'
        db.create_table('socialauth_openidprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('openid_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='openid_profiles', to=orm['auth.User'])),
            ('is_username_valid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('socialauth', ['OpenidProfile'])

        # Adding model 'LinkedInUserProfile'
        db.create_table('socialauth_linkedinuserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('linkedin_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='linkedin_profiles', to=orm['auth.User'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('profile_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('socialauth', ['LinkedInUserProfile'])

        # Adding model 'TwitterUserProfile'
        db.create_table('socialauth_twitteruserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='twitter_profiles', to=orm['auth.User'])),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('profile_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
        ))
        db.send_create_signal('socialauth', ['TwitterUserProfile'])

        # Adding model 'FacebookUserProfile'
        db.create_table('socialauth_facebookuserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='facebook_profiles', to=orm['auth.User'])),
            ('profile_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('profile_image_url_big', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('profile_image_url_small', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('about_me', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
        ))
        db.send_create_signal('socialauth', ['FacebookUserProfile'])


    def backwards(self, orm):
        
        # Deleting model 'AuthMeta'
        db.delete_table('socialauth_authmeta')

        # Deleting model 'OpenidProfile'
        db.delete_table('socialauth_openidprofile')

        # Deleting model 'LinkedInUserProfile'
        db.delete_table('socialauth_linkedinuserprofile')

        # Deleting model 'TwitterUserProfile'
        db.delete_table('socialauth_twitteruserprofile')

        # Deleting model 'FacebookUserProfile'
        db.delete_table('socialauth_facebookuserprofile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'socialauth.authmeta': {
            'Meta': {'object_name': 'AuthMeta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_email_filled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_profile_modified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'socialauth.facebookuserprofile': {
            'Meta': {'object_name': 'FacebookUserProfile'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'facebook_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'profile_image_url_big': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'profile_image_url_small': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facebook_profiles'", 'to': "orm['auth.User']"})
        },
        'socialauth.linkedinuserprofile': {
            'Meta': {'object_name': 'LinkedInUserProfile'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'linkedin_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'linkedin_profiles'", 'to': "orm['auth.User']"})
        },
        'socialauth.openidprofile': {
            'Meta': {'object_name': 'OpenidProfile'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_username_valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'openid_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'openid_profiles'", 'to': "orm['auth.User']"})
        },
        'socialauth.twitteruserprofile': {
            'Meta': {'object_name': 'TwitterUserProfile'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'twitter_profiles'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['socialauth']
