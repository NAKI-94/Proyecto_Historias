# hc_maquillaje/forms.py
from django import forms
from .models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['fecha', 'descripcion', 'remitido_por', 'ocupacion', 'hijos', 
                  'medicamentos', 'enfermedades', 'cx', 'motivo_consulta', 
                  'cejas_anteriores', 'lineas_anteriores', 'labios_anteriores', 
                  'tiempo_anteriores', 'tiempo_elaborado', 'color_anterior', 
                  'alergias', 'observaciones', 'correcciones', 
                  'cejas_actuales', 'color_actual', 'neutralizar', 
                  'lineas_superior', 'lineas_inferior', 'labios_actuales', 
                  'anestesia_topica', 'anestesia_inyectada', 
                  'material_desechable', 'resultado_satisfactorio', 
                  'costo_maquillaje', 'retoque_fecha']
        
        # Agrega el campo paciente como oculto
        widgets = {
            'paciente': forms.HiddenInput()
        }
