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
    descripcion = models.TextField()
    def __str__(self):
        return f"Historia Clínica de {self.paciente.nombre_completo} - {self.fecha}"
    
    # Primer formulario
    remitido_por = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    hijos = models.IntegerField()
    medicamentos = models.TextField()
    enfermedades = models.TextField()
    cx = models.TextField()  # Cirugías
    motivo_consulta = models.TextField()

    # Maquillaje Anterior
    cejas_anteriores = models.BooleanField(default=False)
    lineas_anteriores = models.BooleanField(default=False)
    labios_anteriores = models.BooleanField(default=False)
    tiempo_anteriores = models.BooleanField(default=False)
    tiempo_elaborado = models.CharField(max_length=255)
    color_anterior = models.CharField(max_length=255)
    alergias = models.TextField()
    observaciones = models.TextField()
    correcciones = models.TextField()

    # Maquillaje Actual
    cejas_actuales = models.BooleanField(default=False)
    color_actual = models.CharField(max_length=255)
    neutralizar = models.BooleanField(default=False)
    lineas_superior = models.BooleanField(default=False)
    lineas_inferior = models.BooleanField(default=False)
    labios_actuales = models.BooleanField(default=False)
    anestesia_topica = models.BooleanField(default=False)
    anestesia_inyectada = models.BooleanField(default=False)
    material_desechable = models.CharField(max_length=255)
    resultado_satisfactorio = models.TextField()

    # Otros campos
    costo_maquillaje = models.IntegerField()
    retoque_fecha = models.DateField()

    def __str__(self):
        return f"Historia Clínica de {self.paciente.nombre_completo}"
