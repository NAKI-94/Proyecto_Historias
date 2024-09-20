from django.urls import path
from .views import crear_historia_clinica, HistoriaClinicaListView,HistoriaClinicaUpdateView,HistoriaClinicaDetailView

app_name = 'hc_maquillaje'  # Define el espacio de nombres aquí

urlpatterns = [
    path('crear/<int:paciente_id>/', crear_historia_clinica, name='crear_historia_clinica'),

    path('lista/<int:paciente_id>/', HistoriaClinicaListView.as_view(), name='historia_clinica_list'),

    path('editar/<int:pk>/', HistoriaClinicaUpdateView.as_view(), name='historia_clinica_edit'),  # Asegúrate de que esta línea esté presente

     path('historia/<int:pk>/', HistoriaClinicaDetailView.as_view(), name='ver_historia_clinica'),



]
