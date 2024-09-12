from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from .forms import PacienteForm

# Lista de pacientes
def listar_pacientes(request):
    search_query = request.GET.get('search', '')
    if search_query:
        pacientes = Paciente.objects.filter(identificacion__icontains=search_query)
    else:
        pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

# Crear un paciente
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')  # Redirige a la página principal o donde desees
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

# Modificar un paciente
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/editar_paciente.html', {'form': form, 'paciente': paciente})
#ELIMINAR
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'pacientes/eliminar_paciente.html', {'paciente': paciente})

#VER PACIENTE 
def detalle_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'pacientes/detalle_paciente.html', {'paciente': paciente})