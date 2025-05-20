from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

USER_TYPES = (
    ("0", "Administrador"),
    ("1", "Publicador"),
    ("2", "Editor"),
    ("3", "Lector")
)

#BMA por bajo - medio - alto
ESCALA_BMA = (
    ("0", "IMPLEMENTACION"),
    ("1", "BAJO"),
    ("2", "MEDIO"),
    ("3", "ALTO"),
    ("4", "SIN DEFINIR"),
    ("-1", "SIN ASIGNAR"),
)

ESCALA_PRIORIZACION = (
    ("0", "POR DEFINIR"),
    ("1", "INCIDENCIA"),
    ("2", "INFORMAR"),
    ("-1", "SIN ASIGNAR"),
)

ESCALA_SERVICIO = (
    ("0", "S"),
    ("1", "M"),
    ("2", "L"),
    ("-1", "SIN ASIGNAR"),
)

ESCALA_ESG = (
    ("0", "IMPLEMENTACION"),
    ("1", "E"),
    ("2", "S"),
    ("3", "G"),
    ("4", "N/A"),
    ("-1", "SIN ASIGNAR"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo_usuario = models.CharField(choices=USER_TYPES, max_length=1, default="0")
    telefono = models.CharField(max_length=10, null=True, blank=True)
    status = models.BooleanField(default=True, blank=True, null=True)
    cambiar_pass = models.BooleanField(default=True, blank=True, null=True)

class Comentario(models.Model):
    fecha_creacion = models.DateField(default=timezone.now, null=True, blank=True)
    referencia = models.CharField(max_length=100, null=True, blank=True)
    informacion = models.CharField(max_length=500, null=True, blank=True)
    autor = models.ForeignKey(Profile, on_delete=models.DO_NOTHING , blank=True, null=True)

class Regulacion(models.Model):
    correlativo = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    esg = models.CharField(choices=ESCALA_ESG, max_length=2, default="-1")
    factibilidad = models.CharField(choices=ESCALA_BMA, max_length=2, default="-1")
    impacto = models.CharField(choices=ESCALA_BMA, max_length=2, default="-1")
    impacto_publico = models.CharField(choices=ESCALA_BMA, max_length=2, default="-1")
    priorizacion = models.CharField(choices=ESCALA_PRIORIZACION, max_length=2, default="-1")
    servicio = models.CharField(choices=ESCALA_SERVICIO, max_length=2, default="-1")
    tipo_act = models.CharField(max_length=200, null=True, blank=True)
    origen = models.CharField(max_length=200, null=True, blank=True)
    resp_gerencial = models.CharField(max_length=200, null=True, blank=True)
    responsable = models.CharField(max_length=200, null=True, blank=True)
    ambito_afectado = models.CharField(max_length=200, null=True, blank=True)
    foco = models.CharField(max_length=200, null=True, blank=True)
    comentarios = models.ManyToManyField(Comentario, blank=True)
    fecha_creacion = models.DateField(default=timezone.now, null=True, blank=True)
    activo = models.BooleanField(default=True, blank=True, null=True)
    estado_tramite = models.CharField(max_length=200, null=True, blank=True)
    fecha_edicion = models.DateTimeField(auto_now=True,blank=True,null=True)
