# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Choices(object):
    STATUS_TICKETS = (
        ('new', u'nuevo'),
        ('in_proccess', u'en proceso'),
        ('wait_for_reply', u'esperando confirmacion'),
        ('finalize', u'finalizado')
    )

    PRIORITY_TICKET = (
        ('low', u'Baja'),
        ('medium', u'Media'),
        ('high', u'Alta')
    )

    AREA_TICKET = (
        ('technical', u'Tecnico'),
        ('commercial', u'Comercial'),
        ('payments', u'Pagos')

    )