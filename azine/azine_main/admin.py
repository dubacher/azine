from django.contrib import admin
from azine_main.models import Job, JobState, Application, Invitation

class JobAdmin(admin.ModelAdmin):
    pass

class JobStateAdmin(admin.ModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Job, JobAdmin)
admin.site.register(JobState, JobStateAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Invitation)
