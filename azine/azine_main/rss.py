from django.contrib.syndication.views import Feed
from azine_main.models import Job
from django.core.urlresolvers import reverse

class LatestEntriesFeed(Feed):
    title = "Job site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to azine jobs."

    def items(self):
        return Job.objects.order_by('-created')[:5]

    def item_title(self, job):
        return job.title

    def item_description(self, job):
        return job.description
             
    def item_link(self, job):
        return reverse('job_detail', args=[job.pk])
