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

class AddAccountApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()


    def post(self, request, format=None):
        messages_list = []
        account_info  = []
        error_list    = []
        status        = False

        req = request.POST

        if req.get('domain'):
            domain = req.get('domain')

            if req.get('username'):
                username = req.get('username')

                params = {
                    'domain': domain,
                    'username': username
                }
                
            else:
                params = {
                    'domain': domain
                }

            response = requests.get('http://nodo1.magiosteam.com:8000/api/v1/create_account/', params=params)
            response = response.json()

            status        = response['status']
            messages_list = response['message']
            account_info  = response['response']
            error_list    = response['error']

        else:
            status        = False
            messages_list = 'No domain found.'
            account_info  = None
            error_list    = '[ ERROR ] No domain provided.' 

        response = {
            'status'  : status,
            'message' : messages_list,
            'response': account_info,
            'error'   : error_list
        }

        return Response(response)