from django import forms
from .models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'  # Asegúrate de que todos los campos que necesitas estén incluidos
