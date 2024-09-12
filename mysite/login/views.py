from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def pagina_protegida(request):
    return render(request, 'login/protegida.html')

@login_required
def crear_paciente(request):
    # Lógica para crear pacientes
    return render(request, 'pacientes/crear_paciente.html')

def homepage(request):
    return render(request, 'login/homepage.html')

