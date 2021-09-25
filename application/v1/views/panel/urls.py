# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# Custom
from v1.views.panel.password             import PasswordPanelApiView
from v1.views.panel.login                import LoginAccountApiView

urlpatterns = [
    path('login/', LoginAccountApiView.as_view(), name='login_account_api_view'),
    path('password/', PasswordPanelApiView.as_view(), name='password_panel'),
]

