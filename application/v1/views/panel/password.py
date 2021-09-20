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
from schemas.models.nodos           import Nodos

class PasswordPanelApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()


    def get(self,request, format=None):
        req = request.GET

        username = req.get('username')
        password = req.get('password')
        actual_password = req.get('actual_password')
        server = Nodos.objects.get(username=username)


        if server:
            params = {
                'username' : username,
                'password' : password,
                'actual_password' : actual_password
            }

            response = requests.get('http://{nodo}:8000/api/v1/change_password/'.format(nodo=server.nodo), params=params)
            
        else:
            response = {
                'status'  : False,
                'message' : 'No username found.',
                'response': None,
                'error'   : '[ ERROR ] No username provided'
            }

        response = response.json()
        return Response(response)



