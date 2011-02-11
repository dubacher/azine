from django.contrib import admin
from azine_main.models import Job, JobState, Skill, Application, Invitation
from mptt.admin import MPTTModelAdmin

class JobAdmin(admin.ModelAdmin):
    pass

class JobStateAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(MPTTModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('invitation_code', 'created', 'from_user', 'to_email', 'created_user')
    
    def save_model(self, request, obj, form, change):
        obj.from_user = request.user
        super(InvitationAdmin, self).save_model(request, obj, form, change)
    
admin.site.register(Job, JobAdmin)
admin.site.register(JobState, JobStateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Invitation, InvitationAdmin)
