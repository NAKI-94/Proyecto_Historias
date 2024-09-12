from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pacientes, name='listar_pacientes'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('<int:pk>/', views.detalle_paciente, name='detalle_paciente'),
    path('<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('<int:pk>/eliminar/', views.eliminar_paciente, name='eliminar_paciente'),
]
