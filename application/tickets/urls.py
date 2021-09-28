# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


#App

urlpatterns = [
    path('login/', include('tickets.views.urls')),

]

