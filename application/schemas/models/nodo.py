# -*- coding: utf-8 -*-
# Python
from __future__                 import unicode_literals

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _


class Nodo(models.Model):
    name           = models.CharField(verbose_name=_(u'Nombre'), max_length=255)
    ipaddress      = models.CharField(verbose_name=_(u'Direccion IP'), max_length=255)
    creation_date  = models.DateField(verbose_name=_(u'Fecha de creacion'), auto_now_add=True)
    total_accounts = models.IntegerField(verbose_name=_(u'Total de cuentas creadas'), default=0)

    class Meta:
        verbose_name        = _(u"Nodo")
        verbose_name_plural = _(u"Nodos")

    def __str__(self):
        return "{server}".format(server=self.name)

    