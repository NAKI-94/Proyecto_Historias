# hc_maquillaje/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import HistoriaClinica, Paciente
from .forms import HistoriaClinicaForm

def crear_historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            historia_clinica = form.save(commit=False)
            historia_clinica.paciente = paciente
            historia_clinica.save()
            return redirect('hc_maquillaje:historia_clinica_list', paciente_id=paciente.id)
    else:
        form = HistoriaClinicaForm()

    return render(request, 'hc_maquillaje/crear_historia_clinica.html', {'form': form, 'paciente': paciente})

from django.views.generic import ListView
from .models import HistoriaClinica

class HistoriaClinicaListView(ListView):
    model = HistoriaClinica
    template_name = 'hc_maquillaje/historia_clinica_list.html'
    context_object_name = 'historias_clinicas'

    def get_queryset(self):
        paciente_id = self.kwargs.get('paciente_id')
        return HistoriaClinica.objects.filter(paciente_id=paciente_id)

from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import HistoriaClinica

class HistoriaClinicaUpdateView(UpdateView):
    model = HistoriaClinica
    fields = ['fecha', 'descripcion']
    template_name = 'hc_maquillaje/historia_clinica_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('hc_maquillaje:historia_clinica_list', kwargs={'paciente_id': self.object.paciente.id})
