# -*- coding: utf-8 -*-
# Python
from __future__                 import unicode_literals

# Django
from django.db                  import models
from django.db.models.fields import CharField
from django.utils.translation   import ugettext_lazy as _

class History(models.Model):
    creation_date  = models.DateField(verbose_name=_(u'Fecha de creacion'), auto_now_add=True)
    text           = models.TextField(verbose_name=_(u'Historia'), blank=True)

    class Meta:
        verbose_name        = _(u"History")
        verbose_name_plural = _(u"Historys")

    def __str__(self):
        return "{date}".format(date=self.creation_date)

    
    