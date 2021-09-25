# -*- coding: utf-8 -*-

# Python
import socket
import requests

# Django

# App

class Nexus(object):
	
	def get_account_server(self, domain):

		#Hardcodeado hasta la muerte xd
		hostname = socket.gethostname()
		hostname = hostname.split('.')[1] + '.' home.split('.')[2]
		return "nodo1.{}".format(hostname)
		