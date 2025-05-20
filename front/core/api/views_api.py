from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import datetime
from core.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from core.tasks import *
from django.core.exceptions import ObjectDoesNotExist
import time

class CreateProfesional(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        response = {}

        return Response(response)    