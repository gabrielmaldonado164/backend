# Python
import requests
# Django
from django.conf                   import settings

# Django Rest
from django.contrib.auth.models    import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions    import IsAuthenticated
from rest_framework.response       import Response
from rest_framework.views          import APIView

# App
from schemas.models.nodo           import Nodo
from tools.nexus                   import Nexus

class CreateMysqlDatabaseApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()

    def get(self, request, format=None):
        req      = request.GET
        domain = req.get('domain')
        username = req.get('username')
        dbname   = req.get('dbname')
        nexus    = Nexus()

        if not username:
            response = {
                'status'  : False,
                'message' : 'No username found.',
                'response': None,
                'error'   : '[ ERROR ] No username provided'
            }
            return Response(response)
        

        if not dbname:
            response = {
                'status'  : False,
                'message' : 'No dbname found.',
                'response': None,
                'error'   : '[ ERROR ] No dbname provided'
            }
            return Response(response)

        if not domain:
            response = {
                'status'  : False,
                'message' : 'No domain found.',
                'response': None,
                'error'   : '[ ERROR ] No domain provided'
            }
            return Response(response)
        
        server = Nodo.objects.get(name=nexus.get_account_server(domain))

        params = {
            'username' : username,
            'dbname' : dbname,
        }


        response = requests.get('http://{nodo}:8000/api/v1/panel/mysql/create_database/'.format(nodo=server.name), params=params)
        response = response.json()

        return Response(response)
