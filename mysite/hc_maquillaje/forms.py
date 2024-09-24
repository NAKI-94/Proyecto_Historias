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
            'paciente': forms.HiddenInput(),
            'ocupacion': forms.Textarea(attrs={'class': 'form-control ocupacion-textarea'}),
            'motivo_consulta': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',  # Clases CSS personalizadas
                'rows': 4,  # Número de filas del textarea (opcional)
                'placeholder': 'Describe el motivo de la consulta aquí...',  # Placeholder (opcional)
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',  # Clases CSS personalizadas
                'rows': 4,
                'placeholder': 'Añadir descripción...',
            }),
            'ocupacion': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',  # Clases CSS personalizadas
                'rows': 4,
                'placeholder': 'Especificar ocupación...',
            }),
            'medicamentos': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',  # Clases CSS personalizadas
                'rows': 4,
                'placeholder': 'Medicamentos que esté tomando el paciente...',
            }),
            'enfermedades': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',  # Clases CSS personalizadas
                'rows': 4,
                'placeholder': 'Enfermedades relevantes del paciente...',
            }),
            'cx': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',  # Clases CSS personalizadas
                'rows': 4,
                'placeholder': 'Historial de cirugías (Cx)...',
            }),
            'alergias': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',
                'rows': 4,
                'placeholder': 'Alergias conocidas...',
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',
                'rows': 4,
                'placeholder': 'Observaciones adicionales...',
            }),
            'correcciones': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',
                'rows': 4,
                'placeholder': 'Correcciones realizadas...',
            }),
            'resultado_satisfactorio': forms.Textarea(attrs={
                'class': 'form-control motivo-consulta-textarea',
                'rows': 4,
                'placeholder': 'Describe el resultado satisfactorio aquí...',
            }),
        }
