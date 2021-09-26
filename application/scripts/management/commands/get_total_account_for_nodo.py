# -*- coding: utf-8 -*-

# Python
import requests

# Django
from   django.core.management.base import BaseCommand

# App
from   schemas.models.nodo         import Nodo

class Script(object):
    
    def do(self):
        nodos = Nodo.objects.all()

        for nodo in nodos:

            print("[ INFO ] Obteniendo datos de {nodo}".format(nodo=nodo.name))

            try:
                response = requests.get('http://{nodo}:8000/api/v1/get_total_accounts/'.format(nodo=nodo.name))
                response = response.json()

                total    = response['response']

                nodo.total_accounts = total
                nodo.save()

                print("\t[ OK ] Total de sitios en {nodo}: {total}".format(nodo=nodo, total=total))
            except Exception as e:
                print("\t[ ERROR ] {error}".format(error=e))



class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        worker = Script()
        worker.do()    

