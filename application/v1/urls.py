# -*- coding: utf-8 -*-

# Python

# Django
from django.urls                 import path

# Custom
from v1.views.create_account     import CreateAccountApiView
from v1.views.login              import LoginAccountApiView
# Testing

urlpatterns = [
    path('create_account/', CreateAccountApiView.as_view(), name='create_account_api_view'),
    path('login/', LoginAccountApiView.as_view(), name='login_api_view')
]

