# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                 import path
from django.urls                 import include


# Custom
from v1.views.panel.mysql.create import CreateDatabaseApiView
from v1.views.panel.mysql.list   import ListMySqlDatabasesApiView

urlpatterns = [
    path('create/', CreateDatabaseApiView.as_view(), name='create_mysql_database_api_view'),
    path('list/',   ListMySqlDatabasesApiView.as_view(), name='list_mysql_databases_api_view'),
]

