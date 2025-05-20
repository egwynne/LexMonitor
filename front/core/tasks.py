from core.models import *
from core.utils import *
from main.celery import app
import time

#@app.task(bind=True, name='tasks.core.sync_sii')
#def sync_sii(self, cliente_pk):
#    cliente = Cliente.objects.get(pk=cliente_pk)
#    try:
#        get_buys(cliente.perfil.rut, cliente.clave_sii, cliente.compania.rut)
#        get_sales(cliente.perfil.rut, cliente.clave_sii, cliente.compania.rut)
#        cliente.siisync.status = "Sincronizado"
#        cliente.siisync.save()
#    except:
#        cliente.siisync.status = "Error"
#        cliente.siisync.save()
#    return True