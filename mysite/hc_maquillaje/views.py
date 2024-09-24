# hc_maquillaje/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import HistoriaClinica, Paciente
from .forms import HistoriaClinicaForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy


# Vista para crear una nueva historia clínica
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
    
    context = {
        'form': form,
        'paciente': paciente,
    }

    return render(request, 'hc_maquillaje/crear_historia_clinica.html', context)



# Vista para listar las historias clínicas
class HistoriaClinicaListView(ListView):
    model = HistoriaClinica
    template_name = 'hc_maquillaje/historia_clinica_list.html'
    context_object_name = 'historias_clinicas'

    def get_queryset(self):
        paciente_id = self.kwargs.get('paciente_id')
        return HistoriaClinica.objects.filter(paciente_id=paciente_id)

# Vista para actualizar una historia clínica
class HistoriaClinicaUpdateView(UpdateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'hc_maquillaje/historia_clinica_edit.html'

    def get_success_url(self):
        return reverse_lazy('hc_maquillaje:historia_clinica_list', kwargs={'paciente_id': self.object.paciente.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener la historia clínica actual
        historia_clinica = self.get_object()
        # Obtener el paciente asociado a la historia clínica
        paciente = get_object_or_404(Paciente, id=historia_clinica.paciente_id)
        
        # Agregar el objeto paciente al contexto
        context['paciente'] = paciente  # Cambia 'paciente_id' a 'paciente'
        return context
# Vista para detallar la historia clínica
class HistoriaClinicaDetailView(DetailView):
    model = HistoriaClinica
    template_name = 'hc_maquillaje/historia_clinica_detail.html'  # Plantilla para mostrar los detalles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el paciente asociado a la historia clínica
        historia_clinica = self.get_object()
        paciente = get_object_or_404(Paciente, id=historia_clinica.paciente_id)
        context['paciente'] = paciente
        return context


