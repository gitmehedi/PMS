from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProjectModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    client_name = models.CharField(max_length=50, verbose_name='Client Name',blank=True, null=True)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    actual_start_date = models.DateField(verbose_name='Actual Start Date', null=True, blank=True)
    actual_end_date = models.DateField(verbose_name='Actual End Date', null=True, blank=True)
    start_date = models.DateField(verbose_name='Start Date', null=True, blank=True)
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)
    description = models.TextField(verbose_name='Description')
    status = models.BooleanField(verbose_name='Status', default=True)

    # created_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # updated_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['title']
