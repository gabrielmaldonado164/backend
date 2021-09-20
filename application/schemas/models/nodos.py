# -*- coding: utf-8 -*-
# Python
from __future__                 import unicode_literals

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _


class Nodos(models.Model):
    domain        = models.CharField(verbose_name=_(u'Dominio'), max_length=255)
    nodo          = models.CharField(verbose_name=_(u'Nodo'), max_length=255)
    username      = models.CharField(verbose_name=_(u'Usuario'), max_length=255)

    class Meta:
        verbose_name        = _(u"Nodo")
        verbose_name_plural = _(u"Nodos")

    def __str__(self):
        return "{server}".format(server=self.nodo)