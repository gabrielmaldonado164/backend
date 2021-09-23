# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# App
from v1.views.twpanel.nodo.add           import AddNodesApiView
from v1.views.twpanel.nodo.list          import GetNodesListApiView
#from v1.views.panel.password import PasswordPanelApiView

urlpatterns = [
    path('add-nodos/', AddNodesApiView.as_view(), name='add_nodos'),
    path('list-nodos/', GetNodesListApiView.as_view(), name='list_nodos'),
]

