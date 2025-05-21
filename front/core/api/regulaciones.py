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

class GetCorrelativo(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        response = {}
        try:
            ultimo_objeto = Regulacion.objects.latest('id')
            response["correlativo"] = "  "+ str(ultimo_objeto.correlativo + 1)
        except Regulacion.DoesNotExist:
            response["correlativo"] = "  1"
        
        return Response(response)
    
class CreateRegulacion(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {}
        data = request.data["regulacion"]
        regulacion = Regulacion.objects.create()
        regulacion.correlativo = data.get("correlativo")
        regulacion.nombre = data.get("nombre","Sin Informacion")
        regulacion.esg = data.get("esg","-1")
        regulacion.factibilidad = data.get("factibilidad","-1")
        regulacion.impacto = data.get("impacto","-1")
        regulacion.impacto_publico = data.get("impacto_deb","-1")
        regulacion.priorizacion = data.get("priorizacion","-1")
        regulacion.servicio = data.get("servicio","-1")
        regulacion.tipo_act = data.get("tipo_acti","Sin Informacion")
        regulacion.origen = data.get("origen","Sin Informacion")
        regulacion.resp_gerencial = data.get("responsabilidad_geren","Sin Informacion")
        regulacion.responsable = data.get("prof_respon","Sin Informacion")
        regulacion.ambito_afectado = data.get("ambito_afectado","Sin Informacion")
        regulacion.foco = data.get("foco","Sin Informacion")
        regulacion.fecha_creacion = data.get("fecha_creacion")
        regulacion.estado_tramite = data.get("estado_tramite")
        comentario = Comentario.objects.create()
        comentario.referencia = data.get("referencia")
        comentario.informacion = data.get("comentario")
        comentario.fecha_creacion = data.get("fecha_creacion")
        id_autor = int(data.get("autor_id"))
        autor = Profile.objects.get(user__id=id_autor)
        comentario.autor= autor
        comentario.save()
        regulacion.comentarios.add(comentario) 
        regulacion.save()
        return Response(response)
    
class GetRegulaciones(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {}
        query = Q()
        data = request.data
        if data.get("nombre"):
            query &= Q(nombre__icontains=data.get("nombre"))
        if data.get("estado_tramite"):
            query &= Q(estado_tramite__icontains=data.get("estado_tramite"))
        if data.get("impacto") != "-1":
            query &= Q(impacto=data.get("impacto"))
        if data.get("factibilidad") != "-1":
            query &= Q(factibilidad=data.get("factibilidad"))
        if data.get("servicio") != "-1":
            query &= Q(servicio=data.get("servicio"))
        if data.get("priorizacion") != "-1":
            query &= Q(priorizacion=data.get("priorizacion"))
        if data.get("impacto_publico") != "-1":
            query &= Q(impacto_publico=data.get("impacto_publico"))
        if data.get("esg") != "-1":
            query &= Q(esg=data.get("esg"))
        if data.get("foco"):
            query &= Q(foco=data.get("foco"))
        if data.get("estado") != "-1":
            query &= Q(activo=data.get("estado"))
        regulaciones = Regulacion.objects.filter(query).order_by('correlativo')
        paginator = Paginator(regulaciones, data.get('pageSize', 20))  
        page_number = data.get('pagina', 1)  
        page = paginator.get_page(page_number)
        response["regulaciones"] = [{
            "correlativo" : regulacion.correlativo,
            "nombre" : regulacion.nombre,
            "estado_tramite":regulacion.estado_tramite,
            "id" : regulacion.id,
            "impacto" : regulacion.impacto,
            "impacto_texto" : ESCALA_BMA[int(regulacion.impacto)][1],
            "factibilidad" : regulacion.factibilidad,
            "factibilidad_texto" : ESCALA_BMA[int(regulacion.factibilidad)][1],
            "servicio":regulacion.servicio,
            "servicio_texto":ESCALA_SERVICIO[int(regulacion.servicio)][1],
            "priorizacion":regulacion.priorizacion,
            "priorizacion_texto":ESCALA_PRIORIZACION[int(regulacion.priorizacion)][1],
            "impacto_publico":regulacion.impacto_publico,
            "impacto_publico_texto":ESCALA_BMA[int(regulacion.impacto_publico)][1],
            "esg" : regulacion.esg,
            "esg_texto" : ESCALA_ESG[int(regulacion.esg)][1],
            "comentarios": len(regulacion.comentarios.all()),
            "activo":regulacion.activo,
            "foco":regulacion.foco,
            "fecha":regulacion.fecha_creacion.strftime('%d-%m-%Y'),
            "fecha_edicion":regulacion.fecha_edicion.strftime('%d-%m-%Y'),
        } for regulacion in page]
        response["totalPages"] = paginator.num_pages
        response["currentPage"] = page_number
        return Response(response)
    
class GetRegulacion(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        response = {}
        regulacion_id = request.query_params.get('id')
        if not regulacion_id:
            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        regulacion = Regulacion.objects.get(id=int(regulacion_id))
        ultimo_comentario = regulacion.comentarios.order_by('-id').first()        
        response["regulacion"] = {
            'id': regulacion.id ,
            'correlativo': "  "+str(regulacion.correlativo) ,
            'nombre': regulacion.nombre ,
            'factibilidad': regulacion.factibilidad ,
            'impacto': regulacion.impacto ,
            'priorizacion': regulacion.priorizacion ,
            'servicio': regulacion.servicio ,
            'tipo_acti': regulacion.tipo_act ,
            'responsabilidad_geren': regulacion.resp_gerencial ,
            'prof_respon': regulacion.responsable ,
            'impacto_deb': regulacion.impacto_publico ,
            'origen': regulacion.origen ,
            'ambito_afectado': regulacion.ambito_afectado ,
            'foco': regulacion.foco ,
            'estado': regulacion.activo ,
            'esg': regulacion.esg ,
            'fecha_creacion': regulacion.fecha_creacion ,
            "referencia": ultimo_comentario.referencia if ultimo_comentario else "",
            "comentario": ultimo_comentario.informacion if ultimo_comentario else "",
            "fecha_comentario":ultimo_comentario.fecha_creacion if ultimo_comentario else "",
            "autor_text":ultimo_comentario.autor.user.first_name + " "+ultimo_comentario.autor.user.last_name if ultimo_comentario else "",
            "estado_tramite":regulacion.estado_tramite,
        
        }
        return Response(response)
    

class GetHistorialComentarios(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        response = {}
        regulacion_id = request.query_params.get('id')
        if not regulacion_id:
            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        comentarios = Comentario.objects.filter(regulacion__id=int(regulacion_id))
        comentarios = comentarios.order_by('-id')       
        response["comentarios"] = [{
            'id': comentario.id ,
            "referencia": comentario.referencia if comentario else "",
            "comentario": comentario.informacion if comentario else "",
            "fecha_comentario":comentario.fecha_creacion.strftime('%d-%m-%Y'),
            "autor_text":comentario.autor.user.first_name + " "+comentario.autor.user.last_name if comentario else "",
        } for comentario in comentarios]
        return Response(response)
    
class AgregarComentario(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {}
        
        comentario = Comentario.objects.create()
        comentario.referencia = request.data.get("referencia")
        comentario.informacion = request.data.get("comentario")
        id_autor = int(request.data.get("id_autor"))
        autor = Profile.objects.get(user__id=id_autor)
        comentario.autor = autor
        comentario.save()
        regulacion = Regulacion.objects.get(id=int(request.data.get("id_regulacion")))
        regulacion.comentarios.add(comentario)
        regulacion.save()
        response["date"] = comentario.fecha_creacion
        return Response(response)
    

class EditarRegulacion(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {}
        data = request.data["regulacion"]

        regulacion = Regulacion.objects.get(id=data.get("id"))
        regulacion.nombre = data.get("nombre")
        regulacion.estado_tramite = data.get("estado_tramite")
        regulacion.impacto = data.get("impacto")
        regulacion.factibilidad = data.get("factibilidad")
        regulacion.servicio = data.get("servicio")
        regulacion.priorizacion = data.get("priorizacion")
        regulacion.impacto_publico = data.get("impacto_deb")
        regulacion.esg = data.get("esg")
        regulacion.tipo_act = data.get("tipo_acti")
        regulacion.origen = data.get("origen")
        regulacion.resp_gerencial = data.get("responsabilidad_geren")
        regulacion.responsable = data.get("prof_respon")
        regulacion.ambito_afectado = data.get("ambito_afectado")
        regulacion.foco = data.get("foco")
        regulacion.save()

        return Response(response)
    
class EditarStatusRegulacion(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {}
        data = request.data

        regulacion = Regulacion.objects.get(id=data.get("id"))
        regulacion.activo = data.get('estado')
        regulacion.save()

        return Response(response)
    

class GetDashboards(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {}
        
        regulaciones = Regulacion.objects.filter(activo=True)

        total_regulaciones = regulaciones.count()
        response["total_regulaciones"] = total_regulaciones
        conteo_impactos = {}
        for key, label in ESCALA_BMA:
            cantidad = regulaciones.filter(impacto=key).count()
            conteo_impactos[label] = cantidad
        response["impacto"] = {
            "implementacion": conteo_impactos['IMPLEMENTACION'],
            "bajo": conteo_impactos['BAJO'],
            "medio": conteo_impactos['MEDIO'],
            "alto": conteo_impactos['ALTO'],
            "sin_definir": conteo_impactos['SIN ASIGNAR'],
            "porcentaje_implementacion": round((conteo_impactos['IMPLEMENTACION'] / total_regulaciones) * 100, 2) if total_regulaciones > 0 else 0,
            "porcentaje_bajo": round((conteo_impactos['BAJO'] / total_regulaciones) * 100, 2) if total_regulaciones > 0 else 0,
            "porcentaje_medio": round((conteo_impactos['MEDIO'] / total_regulaciones) * 100, 2) if total_regulaciones > 0 else 0,
            "porcentaje_alto": round((conteo_impactos['ALTO'] / total_regulaciones) * 100, 2) if total_regulaciones > 0 else 0,
            "porcentaje_sin_definir": round((conteo_impactos['SIN ASIGNAR'] / total_regulaciones) * 100, 2) if total_regulaciones > 0 else 0,
        }
        
        return Response(response)
    