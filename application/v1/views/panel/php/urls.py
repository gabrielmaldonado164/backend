# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                import path
from django.urls                import include


# Custom
from v1.views.panel.php.php_ini import PhpIniApiView
from v1.views.panel.php.version import PhpVersionApiView

urlpatterns = [
    path('php_ini/', PhpIniApiView.as_view(), name='php_ini_api_view'),
    path('version/', PhpVersionApiView.as_view(), name='php_version_api_view'),
]

