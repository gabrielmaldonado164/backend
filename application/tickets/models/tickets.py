# -*- coding: utf-8 -*-
# Python
from __future__                 import unicode_literals

# Django
from django.db                  import models
from django.contrib.auth.models import User


from django.utils.translation   import ugettext_lazy as _

# Custom
from tickets.models.choices import Choices
from tickets.models.comments import Comment
from tickets.models.history  import History

class Ticket(models.Model):
    domain          = models.CharField(verbose_name=_(u'Dominio'), max_length=255)
    server          = models.CharField(verbose_name=_(u'Servidor'), max_length=255)
    client_email    = models.CharField(verbose_name=_(u'Email cliente'), max_length=255)
    operator_email  = models.CharField(verbose_name=_(u'Email operador'), max_length=255)
    creation_date   = models.DateField(verbose_name=_(u'Fecha de creacion'), auto_now_add=True)
    last_update     = models.DateTimeField(verbose_name=_(u'Ultima actualizacion'), auto_now=True)
    priority        = models.CharField(verbose_name=_(u'Prioridad'), choices=Choices.PRIORITY_TICKET, max_length=255)
    status          = models.CharField(verbose_name=_(u'Estado'), choices=Choices.STATUS_TICKETS, max_length=255)
    area            = models.CharField(verbose_name=_(u'Area'), choices=Choices.AREA_TICKET, max_length=255)
    operator        = models.CharField(verbose_name=_(u'Operador'), max_length=255)
    respuesta       = models.BooleanField(verbose_name=_(u'Esperando respuesta'), default=False)
    comment         = models.ManyToManyField(Comment, verbose_name=_(u'Comentario'), blank=True)
    history         = models.ManyToManyField(History,verbose_name=_(u'Historia'))

    #operator --> after user or profile

    class Meta:
        verbose_name        = _(u"Ticket")
        verbose_name_plural = _(u"Tickets")

    def __str__(self):
        return "{date} {domain}".format(date=self.creation_date, domain=self.domain)

    
    

