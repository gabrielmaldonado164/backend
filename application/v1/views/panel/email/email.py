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


class EmailPanelApiView(APIView):

    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication
    )

    permission_classes     = ()

    def get(self, request, format=None):
        req = request.GET
        domain = req.get('domain')


        if not domain:
            response = {
                'status'  : False,
                'message' : 'No domain found.',
                'response': None,
                'error'   : '[ ERROR ] No domain provided'
            }
            return Response(response)
        
        server = Nodos.objects.get(domain=domain)

        params = {
            'domain' : domain,
        }

        response = requests.get('http://{nodo}:8000/api/v1/email/get_email_accounts/'.format(nodo=server.name))

        return Response(response)

