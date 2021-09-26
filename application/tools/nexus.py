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

		aux = ''
		for i in range(len(hostname.split('.'))):
			aux += hostname.split('.')[i] + '.'
		return "nodo1.{}".format(aux[:-1])
		