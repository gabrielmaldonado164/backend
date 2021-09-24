# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# App
from v1.views.twpanel.nodos.add          import AddNodesApiView
from v1.views.twpanel.nodos.list         import GetNodesListApiView

from v1.views.twpanel.accounts.add       import AddAccountApiView
from v1.views.twpanel.accounts.list      import GetAccountsListApiView

urlpatterns = [
    path('add-nodos/', AddNodesApiView.as_view(), name='add_nodos'),
    path('list-nodos/', GetNodesListApiView.as_view(), name='list_nodos'),

    path('add-accounts/', AddAccountApiView.as_view(), name="add_accounts")
    path('list-accounts/', GetAccountsListApiView.as_view(), name='list_accounts')
]

