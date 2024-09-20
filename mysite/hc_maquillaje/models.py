from django.db import models
from pacientes.models import Paciente
from django.utils import timezone

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='historias_clinicas_hc_maquillaje'
    )
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)  # Este campo ahora será opcional

    # Primer formulario
    remitido_por = models.CharField(max_length=100, blank=True)
    ocupacion = models.CharField(max_length=100, blank=True)
    hijos = models.IntegerField(blank=True, null=True)  # Para IntegerField, agrega null=True para permitir valores nulos
    medicamentos = models.TextField(max_length=100, blank=True)
    enfermedades = models.TextField(max_length=100, blank=True)
    cx = models.TextField(max_length=100, blank=True)  # Cirugías
    motivo_consulta = models.TextField(max_length=100, blank=True)

    # Maquillaje Anterior
    cejas_anteriores = models.BooleanField(default=False)
    lineas_anteriores = models.BooleanField(default=False)
    labios_anteriores = models.BooleanField(default=False)
    tiempo_anteriores = models.BooleanField(default=False)
    tiempo_elaborado = models.CharField(max_length=100, blank=True)
    color_anterior = models.CharField(max_length=100, blank=True)
    alergias = models.TextField(max_length=100, blank=True)
    observaciones = models.TextField(max_length=100, blank=True)
    correcciones = models.TextField(max_length=100, blank=True)

    # Maquillaje Actual
    cejas_actuales = models.BooleanField(default=False)
    color_actual = models.CharField(max_length=100, blank=True)
    neutralizar = models.BooleanField(default=False)
    lineas_superior = models.BooleanField(default=False)
    lineas_inferior = models.BooleanField(default=False)
    labios_actuales = models.BooleanField(default=False)
    anestesia_topica = models.BooleanField(default=False)
    anestesia_inyectada = models.BooleanField(default=False)
    material_desechable = models.CharField(max_length=100, blank=True)
    resultado_satisfactorio = models.TextField(max_length=100, blank=True)

    # Otros campos
    costo_maquillaje = models.IntegerField(blank=True, null=True)  # Permitir nulos para números
    retoque_fecha = models.DateField(blank=True, null=True)  # Para fechas, usa null=True también
