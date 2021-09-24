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
    path('login/', LoginAccountApiView.as_view(), name='login_api_view'),

    path('panel/', include('v1.views.panel.urls')),
    path('twpanel/', include('v1.views.twpanel.urls')),
    path('email/', include('v1.views.panel.email.urls')),
]

