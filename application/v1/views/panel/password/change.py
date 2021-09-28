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

class PasswordChangeApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()


    def post(self,request, format=None):
        req = request.POST

        domain          = req.get('domain')
        username        = req.get('username')
        actual_password = req.get('actual_password')
        password        = req.get('password')
        
        nexus = Nexus()
        server = Nodo.objects.get(name=nexus.get_account_server(domain=domain))
        
        if server:
            params = {
                'username' : username,
                'password' : password,
                'actual_password' : actual_password
            }

            response = requests.post('http://{nodo}:8000/api/v1/panel/password/change/'.format(nodo=server.name), params=params)
            
        else:
            response = {
                'status'  : False,
                'message' : 'No username found.',
                'response': None,
                'error'   : '[ ERROR ] No username provided'
            }

        response = response.json()
        
        return Response(response)



