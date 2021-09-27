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

#Custom
from schemas.models.nodo           import Nodo
from tools.nexus                   import Nexus

class ListMySqlDatabasesApiView(APIView):

    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()

    def get(self, request, format=None):
        req      = request.GET
        username = req.get('username')
        domain   = req.get('domain')
        nexus    = Nexus()

        if not username or not domain:
            response = {
                'status'  : False,
                'message' : 'No username / domain found.',
                'response': None,
                'error'   : '[ ERROR ] No username / domain provided'
            }
            return Response(response)
        
        server = Nodo.objects.get(name=nexus.get_account_server(username))

        params = {
            'username' : username,
        }

        response = requests.get('http://{nodo}:8000/api/v1/panel/mysql/get_databases/'.format(nodo=server.name), params=params)
        response = response.json()

        return Response(response)

