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
from django.db.models import Q, F
from django.core.paginator import Paginator
from rest_framework import status

class GetUsers(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        response = {}
        query = Q()
        nombre = request.data.get("nombre")
        if nombre:
            query &= (Q(user__first_name__icontains=nombre) )
        apellido = request.data.get("apellido")
        if apellido:
            query &= (Q(user__last_name__icontains=apellido) )
        if request.data.get("correo"):
            query &= Q(user__email__icontains=request.data.get("correo"))
        if request.data.get("estado") != "-1":
            active = request.data.get("estado")
            query &= Q(status=active)
        tipo_user = request.data.get("tipo_usuario")
        if tipo_user != "-1":
            query &= Q(tipo_usuario=tipo_user)
        users = Profile.objects.filter(query).order_by('id')
        paginator = Paginator(users, request.data.get('pageSize', 20)) 
        page_number = request.data.get('pagina', 1)  
        page = paginator.get_page(page_number)
        response["usuarios"] = [{
            "id": user.id,
            "nombre" : user.user.first_name,
            "apellido" : user.user.last_name,
            "correo" : user.user.email,
            "telefono" : user.telefono,
            "tipo" : user.tipo_usuario,
            "tipo_name" : USER_TYPES[int(user.tipo_usuario)][1],
            "status" : user.status
        } for user in page]
        response["totalPages"] = paginator.num_pages
        response["currentPage"] = page_number
        return Response(response)
    
class CreateUser(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None, source=None):
        response = {}
        user = User.objects.create(
            first_name=request.data["nombre"],
            last_name=request.data["apellido"],
            email=request.data["correo"],
            username=request.data["correo"],
            password=request.data["pass"],
        )
        user.set_password(request.data["pass"])
        user.save()
        usuario = Profile.objects.create(
            user=user,
            tipo_usuario=request.data["tipo"],
            telefono=request.data["telefono"],
        )
        usuario.save()
        
        response = {
            "HTTP_200_OK": "¡Datos Ingresados Correctamente!"
        }
        return Response(response)

class EditUser(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None, source=None):
        response = {}
        data = request.data.get('editar_user')
        print(data)
        profile = Profile.objects.get(id=data.get("id"))
        profile.user.first_name = data.get("nombre")
        profile.user.last_name = data.get("apellido")
        profile.user.email = data.get("correo")
        profile.tipo_usuario = data.get("tipo")
        profile.telefono = data.get("telefono")
        profile.user.save()
        profile.save()
        
        response = {
            "HTTP_200_OK": "¡Datos Ingresados Correctamente!"
        }
        return Response(response)
    

class CambiarStatusUsers(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None, source=None):
        response = {}
        user = Profile.objects.get(id=request.data["id_user"])
        user.status =request.data["new_status"]
        user.save()
        response = {
            "HTTP_200_OK": "¡Datos Ingresados Correctamente!"
        }
        return Response(response)