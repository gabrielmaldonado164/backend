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
        nodos = Nodo.objects.all()
        
        response = {
            'status'  : True,
            'message' : None,
            'response': nodos,
            'error'   : None
        }
        
        return Response(response)



