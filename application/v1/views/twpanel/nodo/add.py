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

class AddNodesApiView(APIView):
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()


    def post(self,request, format=None):
        req       = request.POST
        name      = req.get('name')
        ipaddress = req.get('ipaddress')

        nodo = Nodo.objects.create(
            name      = name,
            ipaddress = ipaddress
        )
        
        nodo.save();

        response = {
            'status'  : True,
            'message' : 'Nodo agregado correctamente.',
            'response': None,
            'error'   : None
        }
        
        return Response(response)



