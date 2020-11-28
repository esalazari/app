from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    usuario_id = models.BigIntegerField(primary_key=True)
    usuario_nombre = models.CharField(unique=True, max_length=50)
    usuario_password = models.CharField(max_length=255)
    usuario_tipo = models.CharField(max_length=15)

    class Meta:
        #managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.usuario_nombre


class Solicitud(models.Model):
    solicitud_id = models.BigIntegerField(primary_key=True)
    solicitud_cantidad = models.BigIntegerField()
    solicitud_tipo = models.CharField(max_length=15)
    solicitud_ubicacion = models.CharField(max_length=1000)
    licitacion_productor_inicio = models.DateTimeField(auto_now=True)
    licitacion_productor_fin = models.DateField(blank=True, null=True)
    licitacion_transporte_inicio = models.DateField(blank=True, null=True)
    licitacion_transporte_fin = models.DateField(blank=True, null=True)
    cliente_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    solicitud_fecha = models.DateField()
    solicitud_comentario = models.CharField(max_length=4000)

    def __str__(self):
        return self.solicitud_id

    class Meta:
        #managed = False
        db_table = 'solicitud'
