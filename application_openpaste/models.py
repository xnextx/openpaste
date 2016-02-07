#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Inset-Wklejka
class Inset(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, default=None)
    content = models.TextField(verbose_name="Content", max_length=10000000)
    private = models.BooleanField(verbose_name="Private", default=False, blank=True)
    url_private = models.CharField(verbose_name="URL name", blank=True, max_length=10000)
    date_added = models.DateTimeField(verbose_name="Date added", blank=True)

    def __unicode__(self):
        return u"%s" % (self.owner)
