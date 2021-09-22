# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                import path
from django.urls                import include


# Custom
from v1.views.panel.email.get_email_accounts    import GetEmailAccountsApiView
from v1.views.panel.email.create_email_account  import CreateEmailAccountsApiView
urlpatterns = [
    path('get_email_accounts/', GetEmailAccountsApiView.as_view(), name='email_list_account'),
    path('create_email_account/', CreateEmailAccountsApiView.as_view(), name='create_email_account'),
]
