from django.db import models

class Paciente(models.Model):
    nombre_completo = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    ocupacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='historias_clinicas_pacientes'
    )
    fecha = models.DateField()
    descripcion = models.TextField()