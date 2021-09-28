# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


#App
from tickets.views.login  import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login_account_view'),
]

