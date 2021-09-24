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

class GetNodesListApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()


    def get(self,request, format=None):
        nodos = Nodo.objects.all().values()
        
        account_list = []
        for nodo in nodos:
            response = requests.get("http://{nodo}:8000/api/v1/list-accounts/")
            response = response.json()

            if response['status']:
                account_list.append(
                    {
                        'nodo'      : nodo.name,
                        'ipaddress' : nodo.ip,
                        'accounts'  : response['response']
                    }
                )

        response = {
            'status'  : True,
            'message' : None,
            'response': account_list,
            'error'   : None
        }
        
        return Response(response)