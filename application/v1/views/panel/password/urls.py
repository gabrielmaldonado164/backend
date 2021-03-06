# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                    import path
from django.urls                    import include

# App
from v1.views.panel.password.change import PasswordChangeApiView

urlpatterns = [
    path('change/', PasswordChangeApiView.as_view(), name='password_change_api_view'),
]

