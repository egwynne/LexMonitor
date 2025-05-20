from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from core.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from core.tasks import *
from datetime import datetime, timedelta
from django.conf import settings
import requests




class testing(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None, source=None):
        response = {}
        response = requests.get("https://serviciospolar.safeware.cl/api/paises-con-tasas/")

        if response.status_code == 200:
            # Si la solicitud fue exitosa, podemos imprimir el contenido de la respuesta
            print(response.text)
        else:
            # Si la solicitud no fue exitosa, imprimimos el código de estado de la respuesta
            print("Error:", response.status_code)
        return Response(response)
    
