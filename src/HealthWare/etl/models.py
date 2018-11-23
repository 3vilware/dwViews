
from django.db import models

# universal select for different databases

class Query(models.Model):
    database = models.CharField(max_length=200)
    select = models.CharField(max_length=200)
    having = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    sort = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    nestedSelect = models.CharField(max_length=200)


class Establecimientos(models.Model):
    ESTABLECIMIENTO = models.CharField(max_length=25)
    INSTITUCION = models.CharField(max_length=25)
    LICENCIA = models.CharField(max_length=25)
    LICENCIA_FECHA_EXPEDICION = models.CharField(max_length=25)
    ENTIDAD_FEDERATIVA = models.CharField(max_length=25)
    CODIGO_ENTIDAD_FEDERATIVA = models.IntegerField()
    PROCURACION = models.BooleanField(default=False)
    TRASPLANTE_AMNIOS = models.BooleanField(default=False)
    TRASPLANTE_CARA = models.BooleanField(default=False)
    TRASPLANTE_CELULAS_PANCREATICAS = models.BooleanField(default=False)
    TRASPLANTE_CORAZON = models.BooleanField(default=False)
    TRASPLANTE_CORNEA = models.BooleanField(default=False)
    TRASPLANTE_EXTREMIDADES = models.BooleanField(default=False)
    TRASPLANTE_HUESO = models.BooleanField(default=False)
    TRASPLANTE_INTESTINO = models.BooleanField(default=False)
    TRASPLANTE_MANO = models.BooleanField(default=False)
    TRASPLANTE_PANCREAS = models.BooleanField(default=False)
    TRASPLANTE_PARATIROIDES = models.BooleanField(default=False)
    TRASPLANTE_PIEL = models.BooleanField(default=False)
    TRASPLANTE_PULMON = models.BooleanField(default=False)
    TRASPLANTE_RINON = models.BooleanField(default=False)
    TRASPLANTE_VALVULAS = models.BooleanField(default=False)
    BANCO_AMNIOS = models.BooleanField(default=False)
    BANCO_CORNEA = models.BooleanField(default=False)
    BANCO_HUESO = models.BooleanField(default=False)
    BANCO_PIEL = models.BooleanField(default=False)

