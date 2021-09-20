# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# Custom
from v1.views.panel.password import PasswordPanelApiView

urlpatterns = [
    path('password/', PasswordPanelApiView.as_view(), name='password_panel'),
]

