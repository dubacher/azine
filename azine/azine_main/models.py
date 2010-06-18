from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext

class UserProfile(models.Model):
    cv_url = models.URLField()
    user = models.ForeignKey(User, unique=True)

class JobState(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __unicode__(self):
        return self.name
        
class Job(models.Model):
    
    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')
        ordering = ['-created']
    
    title = models.CharField(_('title'), max_length=255, null=False, blank=False)
    slug = models.SlugField(null=True, blank=True, editable=False)
    description = models.TextField(_('description'), null=False, blank=False)
    required_skills = models.TextField(_('required skills'), null=False, blank=False)
    user = models.ForeignKey(User, verbose_name=_('user'))
    state = models.ForeignKey(JobState, verbose_name=_('state'))
    start_date = models.DateField(null=False, blank=False) # Startdatum des Engagements
    end_date = models.DateField(null=True, blank=True, ) # Enddatum des Engagements
    fte = models.IntegerField() #min_value=0, max_value=100) # Stellenprozente
    # attachment: { type: string(255), notnull: false } # Name eines allfaelligem Attachments
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.title
    
class Application(models.Model):
    
    RATE_DAILY = 1
    RATE_HOURLY = 2
    RATE_CHOICES = (
        (RATE_DAILY, _('daily')),
        (RATE_HOURLY, _('hourly')),
    )
    
    job = models.ForeignKey(Job, editable=False)
    applicant = models.ForeignKey(User, editable=False)  
    text = models.TextField(_('application text'), null=False, blank=False) # Bewerbungstext

    requested_rate = models.DecimalField(max_digits=6, decimal_places=2) # Rate die der Freelancer will
    rate_type = models.IntegerField(choices=RATE_CHOICES) # Tages oder Stundensatz
    
    # cv_attachment: { type: blob } # Blob mit allfaelligem CV-Attachment.

    def __unicode__(self):
        return ugettext('%(user)s applied for %(job)s' % {'user': self.applicant.__unicode__(), 'job': self.job.__unicode__()}) 
