# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext
from django.core.validators import RegexValidator
from user_profiles.models import UserProfileBase
from random_id import random_id
from mptt.models import MPTTModel
import hashlib

INVITATION_CODE_LENGTH = 10
ZIP_VALIDATOR = RegexValidator(r'^[0-9]{4}$');
PHONE_VALIDATOR = RegexValidator(r'^[0-9\(\)\+\ ]{10,}$');


class AcceptField(models.BooleanField):
    def formfield(self, **kwargs):
        kwargs['required'] = True
        return super(AcceptField, self).formfield(**kwargs)


class ContactInformation(UserProfileBase):
    user = models.ForeignKey(User, verbose_name=_('user'), editable=False)
    company = models.CharField(_('company'), max_length=255, null=True, blank=True)
    title = models.CharField(_('title'), max_length=64, editable=False, blank=True) #choices=settings.USER_CONTACT_TITLE_CHOICES
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    function = models.CharField(_('function'), max_length=255, blank=True, null=True, help_text=_('e.g. consulting engineers, agent'))
    email = models.EmailField(_('email'), max_length=75)
    email_activated = models.BooleanField(_('email activated'), default=False, editable=False)
    website = models.URLField(null=True, blank=True)
    address1 = models.CharField(_('address'), max_length=255)
    address2 = models.CharField(_('address line 2'), max_length=255, null=True, blank=True)
    zip = models.CharField(_('zip'), max_length=6, validators=[ZIP_VALIDATOR,])
    city = models.CharField(_('city'), max_length=255)
    phone = models.CharField(_('phone'), max_length=255, validators=[PHONE_VALIDATOR,], null=True, blank=True)
    phone_mobile = models.CharField(_('phone (mobile)'), max_length=255, validators=[PHONE_VALIDATOR,], null=True, blank=True)
    fax = models.CharField(_('fax'), max_length=255, validators=[PHONE_VALIDATOR,], null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_created_by', verbose_name=_('created by'), editable=False)
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_modified_by', verbose_name=_('modified by'), editable=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    is_visible = models.BooleanField(editable=False, default=True)
    is_user_profile = models.BooleanField(_('is user profile'), editable=False, default=False)

    accept_terms = models.BooleanField(_('Yes, I accept the %(terms_of_service_link)s'), null=False, blank=False)
    #AcceptField(_('Yes, I accept the %(terms_of_service_link)s'), null=False, blank=False)

    email_info = models.BooleanField(_('Yes, I would like to receive email notifications'), editable=True, default=True)


class UserProfile(ContactInformation):
    class Meta:
        proxy = True


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


class Skill(MPTTModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
        unique_together = ('name', 'parent')

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
