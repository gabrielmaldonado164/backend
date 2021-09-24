# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# App
#from v1.views.twpanel.nodos.add           import AddNodesApiView
from v1.views.twpanel.nodos.list          import GetNodesListApiView

urlpatterns = [
    #path('add-nodos/', AddNodesApiView.as_view(), name='add_nodos'),
    path('list-nodos/', GetNodesListApiView.as_view(), name='list_nodos'),
]

