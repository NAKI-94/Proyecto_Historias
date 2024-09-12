from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_completo', 'identificacion', 'edad', 'genero', 'telefono', 'direccion', 'correo_electronico', 'ocupacion']
