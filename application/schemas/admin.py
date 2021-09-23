# -*- coding: utf-8 -*-

# Python

# Django
from django.contrib      import admin

# App
from schemas.models.nodo import Nodo


# Registers

admin.site.register(Nodo)