# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContactInformation'
        db.create_table('azine_main_contactinformation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('email_activated', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contactinformation_created_by', null=True, to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contactinformation_modified_by', null=True, to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('is_user_profile', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('accept_terms', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('email_info', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('azine_main', ['ContactInformation'])

        # Adding model 'Invitation'
        db.create_table('azine_main_invitation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invitation_from_user', to=orm['auth.User'])),
            ('to_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('personal_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invitation_created_user', null=True, to=orm['auth.User'])),
            ('invitation_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('azine_main', ['Invitation'])

        # Adding model 'JobState'
        db.create_table('azine_main_jobstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('azine_main', ['JobState'])

        # Adding model 'Job'
        db.create_table('azine_main_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('required_skills', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['azine_main.JobState'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fte', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('azine_main', ['Job'])

        # Adding model 'Application'
        db.create_table('azine_main_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['azine_main.Job'])),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('requested_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('rate_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('azine_main', ['Application'])


    def backwards(self, orm):
        
        # Deleting model 'ContactInformation'
        db.delete_table('azine_main_contactinformation')

        # Deleting model 'Invitation'
        db.delete_table('azine_main_invitation')

        # Deleting model 'JobState'
        db.delete_table('azine_main_jobstate')

        # Deleting model 'Job'
        db.delete_table('azine_main_job')

        # Deleting model 'Application'
        db.delete_table('azine_main_application')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'azine_main.application': {
            'Meta': {'object_name': 'Application'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['azine_main.Job']"}),
            'rate_type': ('django.db.models.fields.IntegerField', [], {}),
            'requested_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'azine_main.contactinformation': {
            'Meta': {'object_name': 'ContactInformation'},
            'accept_terms': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contactinformation_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email_activated': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'email_info': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_user_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contactinformation_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'azine_main.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invitation_created_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invitation_from_user'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'personal_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        'azine_main.job': {
            'Meta': {'object_name': 'Job'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fte': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'required_skills': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['azine_main.JobState']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'azine_main.jobstate': {
            'Meta': {'object_name': 'JobState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['azine_main']
