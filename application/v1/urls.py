# -*- coding: utf-8 -*-

# Python

# Django
from django.urls import path
from django.urls import include

# App

urlpatterns = [
    path('panel/', include('v1.views.panel.urls')),
    path('twpanel/', include('v1.views.twpanel.urls')),
]

