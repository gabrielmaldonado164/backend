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


# Custom
from schemas.models.nodo           import Nodo
from tools.nexus                   import Nexus

class PhpVersionApiView(APIView):

    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()

    def get(self,request, format=None):
        req = request.GET

        domain   = req.get('domain')
        username = req.get('username')
        nexus    = Nexus()
        
        print(username)

        if not domain:
            response = {
                'status'  : False,
                'message' : 'No domain found.',
                'response': None,
                'error'   : '[ ERROR ] No domain provided'
            }

            return Response(response)

        if not username:
            response = {
                'status'  : False,
                'message' : 'No username found.',
                'response': None,
                'error'   : '[ ERROR ] No username provided'
            }

            return Response(response)

        server = Nodo.objects.get(name=nexus.get_account_server(domain=domain))
        
        if server:
            params = {
                'username' : username,
            }

            response = requests.get('http://{nodo}:8000/api/v1/panel/php/get_php_version/'.format(nodo=server.name), params=params)
            
        else:
            response = {
                'status'  : False,
                'message' : 'No server found.',
                'response': None,
                'error'   : '[ ERROR ] No server provided'
            }

        response = response.json()
        
        return Response(response)

    def post(self,request, format=None):
        req = request.POST

        domain   = req.get('domain')
        username = req.get('username')
        version  = req.get('version')
        nexus    = Nexus()
        
        print(request.POST)

        if not domain:
            response = {
                'status'  : False,
                'message' : 'No domain found.',
                'response': None,
                'error'   : '[ ERROR ] No domain provided'
            }

            return Response(response)

        if not username:
            response = {
                'status'  : False,
                'message' : 'No username found.',
                'response': None,
                'error'   : '[ ERROR ] No username provided'
            }

            return Response(response)

        if not version:
            response = {
                'status'  : False,
                'message' : 'No version found.',
                'response': None,
                'error'   : '[ ERROR ] No version provided'
            }

            return Response(response)
        server = Nodo.objects.get(name=nexus.get_account_server(domain=domain))
        
        if server:
            params = {
                'username' : username,
                'version'  : version
            }

            response = requests.post('http://{nodo}:8000/api/v1/panel/php/change_php_version/'.format(nodo=server.name), data=params)
            
        else:
            response = {
                'status'  : False,
                'message' : 'No server found.',
                'response': None,
                'error'   : '[ ERROR ] No server provided'
            }

        response = response.json()
        
        return Response(response)



