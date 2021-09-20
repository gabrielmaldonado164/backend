# -*- coding: utf-8 -*-

# Python

# Django
from django.urls                 import path
from django.urls                 import include

# Custom
from v1.views.create_account     import CreateAccountApiView
from v1.views.login              import LoginAccountApiView
# Testing

urlpatterns = [
    path('create_account/', CreateAccountApiView.as_view(), name='create_account_api_view'),
    path('login/', LoginAccountApiView.as_view(), name='login_api_view'),

    path('panel/', include('v1.views.panel.urls')),
    path('email/', include('v1.views.panel.email.urls')),
]

