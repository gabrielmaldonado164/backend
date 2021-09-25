# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# Custom
from v1.views.panel.login                import LoginAccountApiView

urlpatterns = [
    path('login/', LoginAccountApiView.as_view(), name='login_account_api_view'),

    path('email/',    include('v1.views.panel.email.urls')),
    path('mysql/',    include('v1.views.panel.mysql.urls')),
    path('password/', include('v1.views.panel.password.urls')),
    path('php/',      include('v1.views.panel.php.urls')),

]

