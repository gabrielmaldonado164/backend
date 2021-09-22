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

from schemas.models.nodos import Nodos

class CreateEmailAccountsApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()

    def get(self, request, format=None):
        req = request.GET
        domain = req.get('domain')
        username = req.get('username')
        password = req.get('password')
        quota = None

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

        if not password:
            response = {
                'status'  : False,
                'message' : 'No password found.',
                'response': None,
                'error'   : '[ ERROR ] No password provided'
            }
            return Response(response)

        if req.get('quota'):
            quota = req.get('quota')
        

        server = Nodos.objects.get(domain=domain)
        
        params = {
            'domain' : domain,
            'username' : username,
            'password' : password,
            'quota' : quota
        }


        response = requests.get('http://{nodo}:8000/api/v1/email/create_email_account/'.format(nodo=server.nodo), params=params)
        response = response.json()

        return Response(response)