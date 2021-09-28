# -*- coding: utf-8 -*-
# Python
from __future__                 import unicode_literals

# Django
from django.db                  import models
from django.db.models.fields import CharField
from django.utils.translation   import ugettext_lazy as _


class Comment(models.Model):
    creation_date  = models.DateField(verbose_name=_(u'Fecha de creacion'), auto_now_add=True)
    text           = models.TextField(verbose_name=_(u'Comentario'), max_length=255, blank=True)
    #operator

    class Meta:
        verbose_name        = _(u"Comentario")
        verbose_name_plural = _(u"Comentarios")

    def __str__(self):
        return "{date} ".format(date=self.creation_date)

    
    

 
    
