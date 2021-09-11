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

class LoginAccountApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()


    def get(self, request, format=None):
        req    = request.GET
        domain = None

        if req.get('domain'):
            domain = req.get('domain')
        username = req.get('username')
        password = req.get('password')

        if domain:
            params = {
                'domain'  : domain,
                'username': username,
                'password': password
            }
            response = requests.get('http://127.0.0.1:8000/api/v1/login/', params=params)
        else:
            params = {
                'username': username,
                'password': password
            }
            response = requests.get('http://127.0.0.1:8000/api/v1/login/', params=params)

        response = response.json()

        return Response(response)