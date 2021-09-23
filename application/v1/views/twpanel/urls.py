# -*- coding: utf-8 -*-

# Python

# Django 
from django.urls                         import path
from django.urls                         import include


# App
from v1.views.twpanel.nodo               import GetNodesListApiView
#from v1.views.panel.password import PasswordPanelApiView

urlpatterns = [
    #path('password/', PasswordPanelApiView.as_view(), name='password_panel'),
    path('list-nodos/', GetNodesListApiView.as_view(), name='list_nodos')
]

