#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Inset-Wklejka
class Inset(models.Model):
    owner = models.ForeignKey(User)
    content = models.CharField(verbose_name="Zawartosc", max_length=1000)

    def __unicode__(self):
        return u"%s" % (self.owner)
