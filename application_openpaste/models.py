#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Inset-Wklejka
class Inset(models.Model):
    owner = models.ForeignKey(User)
    content = models.CharField(verbose_name="Content", max_length=1000)
    private = models.BooleanField(verbose_name="Private", default=False)
    date_added = models.DateTimeField(verbose_name="Date added")

    def __unicode__(self):
        return u"%s" % (self.owner)
