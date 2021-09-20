# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                import path
from django.urls                import include


# Custom
from v1.views.panel.email.email import EmailPanelApiView
urlpatterns = [
    path('get_email_accounts/', EmailPanelApiView.as_view(), name='email_list_account',)
]
