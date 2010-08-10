from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext
from random_id import random_id
import md5

INVITATION_CODE_LENGTH = 10

class UserProfile(models.Model):
    hash = models.CharField(max_length=32, editable=False)
    user = models.ForeignKey(User, unique=True, editable=False)
    first_name = models.CharField(_('first_name'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('last_name'), max_length=255, null=True, blank=True)
    ip_address = models.CharField(_('ip_address'), max_length=128, editable=False)
    cv_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.hash = md5.new(self.user.username).hexdigest()
        super(UserProfile, self).save(*args, **kwargs)

class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name='invitation_from_user', editable=False)
    to_email = models.EmailField(_('e-mail'))
    personal_message = models.TextField(_('personal message'), null=True, blank=True)
    created_user = models.ForeignKey(User, editable=False, related_name='invitation_created_user', null=True)
    invitation_code = models.CharField(max_length=INVITATION_CODE_LENGTH, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invitation_code:
            self.invitation_code = random_id(INVITATION_CODE_LENGTH)
        super(Invitation, self).save(*args, **kwargs)

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
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
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
        


